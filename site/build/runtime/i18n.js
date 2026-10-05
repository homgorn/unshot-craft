/**
 * One i18n runtime for every page.
 *
 * Replaces three unrelated inline mechanisms upstream:
 *   1. gallery/translations.js  -> window.GALLERY_I18N   (ui + cardsZh/En + stylesZh/En)
 *   2. gallery/index.html       -> inline L10N            (11 keys, data-l10n, innerHTML)
 *   3. gallery/showcase.js      -> inline SHOWCASE_L10N   (19 keys, data-i18n)
 *
 * The source of truth is site/locales/<code>/*.json, generated into
 * site/dist/assets/i18n/<code>.js by platform/site/build_site.py. Loading a
 * script rather than fetch()ing JSON keeps the first paint synchronous, which
 * matters because the page has no loading state and a flash of English on a
 * Russian page is exactly the bug we are fixing.
 *
 * Locale is fixed by the URL (/<locale>/library.html), never by localStorage.
 * localStorage only remembers a *preference* for the root redirect.
 *
 * Fallback chain: locale -> en -> the key itself. A half-translated locale
 * degrades to English instead of rendering empty strings.
 */
(function (global) {
  'use strict';

  var DATA = global.__I18N_DATA__ || { locale: 'en', fallback: 'en', locales: [], ns: {} };
  var locale = DATA.locale || 'en';
  var fallback = DATA.fallback || 'en';

  /** Locale-aware lookup with an en -> key fallback chain. */
  function t(ns, key) {
    if (!key) return '';
    var group = DATA.ns[ns];
    if (group && group[locale] && group[locale][key] != null) return group[locale][key];
    if (group && group[fallback] && group[fallback][key] != null) return group[fallback][key];
    return key;
  }

  /**
   * String-only lookup. Card and style entries are objects ({title, description}),
   * and assigning an object to textContent renders "[object Object]". Callers that
   * need a display string must say so.
   */
  function s(ns, key) {
    var v = t(ns, key);
    if (v && typeof v === 'object') return v.title || v.description || '';
    return v == null ? '' : String(v);
  }

  /** True when the active locale uses CJK script, so upstream's zh branches apply. */
  function isCJK() {
    return locale === 'zh' || locale === 'ja' || locale === 'ko';
  }

  function htmlLang() {
    var meta = null;
    for (var i = 0; i < DATA.locales.length; i += 1) {
      if (DATA.locales[i].code === locale) { meta = DATA.locales[i]; break; }
    }
    return (meta && meta.htmlLang) || locale;
  }

  /**
   * Is `code` one of the locales the payload ships?
   *
   * `DATA.locales` is an **array** of `{code, nativeName, htmlLang}` -- the same
   * shape `htmlLang()` iterates a few lines below. The guard this replaces
   * indexed it by code, which is `arr['ru']`, always `undefined`, so the locale
   * was never pushed onto the fallback chain.
   *
   * What that cost, precisely: `legacy().ui` returned the fallback language for
   * every locale on the site. Nothing the page shows went through it -- `app.js`
   * reads chrome with `__I18N__.s('ui', key)`, which indexes `DATA.ns` directly
   * and was never wrong, which is why a `/ru/` page rendered correct Russian
   * with the bug in place. What `legacy()` does feed is the zh/en card and style
   * title tables, which are zh and en on every locale by construction.
   *
   * So this was a silently wrong fallback chain rather than a visibly wrong page,
   * which is the harder kind to find: it survives until something reads
   * `legacy().ui`, at which point every locale shows English and there is nothing
   * in the markup to grep for. `platform/site/check_i18n.js` now pins it.
   */
  function hasLocale(code) {
    if (!code) return false;
    var list = DATA.locales || [];
    if (Object.prototype.toString.call(list) === '[object Array]') {
      for (var i = 0; i < list.length; i += 1) {
        if (list[i] && list[i].code === code) return true;
      }
      return false;
    }
    return Object.prototype.hasOwnProperty.call(list, code);
  }

  /**
   * Adapt our namespaced bundles to the flat shape upstream's app.js expects.
   * This is a compatibility shim, not the API: it exists so app.js stays a
   * minimal patch of the upstream file. app.js is patched by
   * build_site.py, which fails loudly if any patch anchor disappears.
   */
  function legacy() {
    var langs = {};
    var all = [fallback];
    if (hasLocale(locale)) all.push(locale);
    for (var i = 0; i < all.length; i += 1) {
      var code = all[i];
      var ui = (DATA.ns.ui && DATA.ns.ui[code]) || {};
      var cards = (DATA.ns.cards && DATA.ns.cards[code]) || {};
      var styles = (DATA.ns.styles && DATA.ns.styles[code]) || {};
      var cardsTitle = {};
      var cardsDesc = {};
      var stylesTitle = {};
      var stylesDesc = {};
      for (var k in cards) {
        if (!Object.prototype.hasOwnProperty.call(cards, k)) continue;
        var v = cards[k];
        if (v && typeof v === 'object') {
          if (v.title) cardsTitle[k] = v.title;
          if (v.description) cardsDesc[k] = v.description;
        } else {
          cardsTitle[k] = v;
          cardsDesc[k] = v;
        }
      }
      for (var s in styles) {
        if (!Object.prototype.hasOwnProperty.call(styles, s)) continue;
        var sv = styles[s];
        if (sv && typeof sv === 'object') {
          if (sv.title) stylesTitle[s] = sv.title;
          if (sv.description) stylesDesc[s] = sv.description;
        } else {
          stylesTitle[s] = sv;
          stylesDesc[s] = sv;
        }
      }
      langs[code] = {
        ui: ui,
        cards: langs[code] && langs[code].cards || {},
        cardsTitle: cardsTitle,
        cardsDesc: cardsDesc,
        stylesTitle: stylesTitle,
        stylesDesc: stylesDesc
      };
    }
    // Upstream's app.js reaches for these exact names.
    langs[fallback].cardsZh = langs.zh ? langs.zh.cardsTitle : {};
    langs[fallback].cardsEn = langs[fallback].cardsDesc;
    langs[fallback].stylesZh = langs.zh ? langs.zh.stylesTitle : {};
    langs[fallback].stylesEn = langs[fallback].stylesDesc;
    if (!langs.en) langs.en = langs[fallback];
    if (!langs.zh) langs.zh = langs[fallback];
    return {
      ui: langs[locale] ? langs[locale].ui : langs[fallback].ui,
      cardsZh: langs[fallback].cardsZh,
      cardsEn: langs[fallback].cardsEn,
      stylesZh: langs[fallback].stylesZh,
      stylesEn: langs[fallback].stylesEn,
      byLocale: langs
    };
  }

  /**
   * Apply every translation attribute in the document.
   *
   * `fallbackNs` is the namespace a **bare** attribute name resolves against, and
   * it is a property of the page rather than of the runtime. `showcase.js` reads
   * its own strings with `s('showcase', key)`, so on `/ru/showcase.html` a bare
   * `data-i18n="navLibrary"` means `showcase.navLibrary`. Calling this with a
   * hardcoded `'ui'` fallback -- which is what it did at first -- resolved those
   * against `ui`, found nothing, and replaced "Библиотека кадров" with the
   * literal word `navLibrary` on the page, while the card list below stayed
   * correctly translated. `data-ns` always wins; the fallback only applies to
   * upstream's own hand-marked attributes, which carry none.
   */
  function apply(root, fallbackNs) {
    var scope = root || document;
    var def = fallbackNs || 'ui';
    function nsOf(node) { return node.dataset.ns || def; }
    scope.querySelectorAll('[data-i18n]').forEach(function (node) {
      node.textContent = s(nsOf(node), node.dataset.i18n);
    });
    scope.querySelectorAll('[data-i18n-aria-label]').forEach(function (node) {
      node.setAttribute('aria-label', s(nsOf(node), node.dataset.i18nAriaLabel));
    });
    // Attribute-valued copy. `placeholder` is the one that matters: the library's
    // search box is the most prominent text on the page and there was no way to
    // translate it, so on /ru/ it read "Search names, use cases, and styles..."
    // while every card under it was in Russian. A localised site with an
    // English search box is a localised site nobody can search.
    scope.querySelectorAll('[data-i18n-placeholder]').forEach(function (node) {
      node.setAttribute('placeholder', s(nsOf(node), node.dataset.i18nPlaceholder));
    });
    scope.querySelectorAll('[data-i18n-title]').forEach(function (node) {
      node.setAttribute('title', s(nsOf(node), node.dataset.i18nTitle));
    });
    // data-l10n is the upstream index.html contract, always `page`, and may
    // contain markup.
    scope.querySelectorAll('[data-l10n]').forEach(function (node) {
      node.innerHTML = s(node.dataset.ns || 'page', node.dataset.l10n);
    });
  }

  /**
   * Sibling URL for the same page in another locale.
   * /ru/library.html -> /es/library.html#crash-zoom-punch
   * The fragment is preserved: deep links into a card must survive a language
   * switch, otherwise the switcher is unusable for anyone sharing a card.
   */
  function urlFor(code) {
    var path = location.pathname;
    var segs = path.split('/');
    if (segs.length > 2 && segs[1] === locale) segs[1] = code;
    var out = segs.join('/');
    return out + location.search + location.hash;
  }

  /**
   * Re-derive every switcher href from the current URL.
   *
   * Needed because hrefs are computed at mount time, and the fragment can
   * change without a reload: a card deep link, an in-page anchor, or the
   * browser back button. Without this, switching language after jumping to a
   * card silently dropped the fragment and landed the visitor on page top.
   */
  function refreshSwitcher() {
    var host = document.querySelector('[data-locale-switcher]');
    if (!host) return;
    var links = host.querySelectorAll('.locale-item');
    for (var i = 0; i < links.length; i += 1) {
      var code = links[i].getAttribute('data-locale');
      if (code) links[i].setAttribute('href', urlFor(code));
    }
  }

  /** Remember a locale choice for the root redirect only. */
  function remember() {
    try { localStorage.setItem('shotcraft-locale', locale); } catch (e) { /* private mode */ }
  }
  function preferred() {
    try { return localStorage.getItem('shotcraft-locale'); } catch (e) { return null; }
  }

  /**
   * Build the language switcher from data, so adding a locale never means
   * editing three HTML files. Renders into [data-locale-switcher].
   */
  function mountSwitcher() {
    var host = document.querySelector('[data-locale-switcher]');
    if (!host) return;
    var old = host.querySelector('.locale-list');
    if (old) old.remove();
    var current = host.querySelector('[data-locale-current]');
    if (current) current.textContent = locale;
    var list = document.createElement('div');
    list.className = 'locale-list';
    DATA.locales.forEach(function (meta) {
      var a = document.createElement('a');
      a.className = 'locale-item' + (meta.code === locale ? ' is-current' : '');
      a.href = urlFor(meta.code);
      a.setAttribute('data-locale', meta.code);
      a.hreflang = meta.code;
      a.lang = meta.htmlLang || meta.code;
      a.textContent = meta.nativeName;
      if (meta.code === locale) a.setAttribute('aria-current', 'page');
      list.appendChild(a);
    });
    host.appendChild(list);

    // Keyboard and touch: :hover alone is not reachable, and the switcher is
    // the only way to change language, so it must work without a pointer.
    var btn = host.querySelector('.locale-flag');
    if (!btn) return;
    function close() { host.classList.remove('is-open'); btn.setAttribute('aria-expanded', 'false'); }
    function open() { host.classList.add('is-open'); btn.setAttribute('aria-expanded', 'true'); }
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      host.classList.contains('is-open') ? close() : open();
    });
    host.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    document.addEventListener('click', function (e) { if (!host.contains(e.target)) close(); });
    document.addEventListener('focusin', function (e) { if (!host.contains(e.target)) close(); });
    list.addEventListener('focusout', function (e) {
      if (!host.contains(e.relatedTarget)) close();
    });
  }

  // Keep the switcher honest when the fragment changes without a reload.
  window.addEventListener('hashchange', refreshSwitcher);
  window.addEventListener('popstate', refreshSwitcher);

  global.__I18N__ = {
    locale: locale,
    fallback: fallback,
    locales: DATA.locales,
    ns: DATA.ns,
    t: t,
    s: s,
    isCJK: isCJK,
    htmlLang: htmlLang,
    apply: apply,
    legacy: legacy,
    urlFor: urlFor,
    refreshSwitcher: refreshSwitcher,
    prefer: preferred,
    remember: remember,
    mountSwitcher: mountSwitcher
  };

  document.documentElement.lang = htmlLang();
  remember();
})(window);