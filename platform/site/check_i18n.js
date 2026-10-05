/**
 * Does the shipped runtime resolve strings in the page's language?
 *
 *     node platform/site/check_i18n.js [site/dist/assets]
 *
 * What this found
 * ---------------
 * `legacy()` never added the page's locale to its fallback chain:
 *
 *     if (DATA.locales[locale]) all.push(locale);
 *
 * `DATA.locales` is an array, so that is `arr['ru']` -- always `undefined`.
 * `legacy().ui` therefore returned the fallback language on every locale.
 *
 * What it did *not* cause, stated plainly because it is easy to overstate:
 * nothing a reader saw was wrong. `app.js` reads chrome through
 * `__I18N__.s('ui', key)`, which indexes `DATA.ns` directly and was always
 * correct, so a `/ru/` page rendered correct Russian with the bug in place --
 * confirmed by running the full browser suite against the broken build and
 * watching all 119 assertions pass. The strings `legacy()` does feed are the
 * zh/en card and style tables, which are zh and en on every locale anyway.
 *
 * So this was a silently wrong code path rather than a visibly wrong page. That
 * is the harder kind to find, not the easier: it has no symptom to grep for, and
 * the first time anything reads `legacy().ui` every locale on the site turns
 * English in one release. This gate is here so that release has a red build
 * instead of a discovery.
 *
 * Why the browser suite could not cover it
 * ----------------------------------------
 * `selftest.py` drives real Chrome and asserts the DOM. The DOM is populated
 * through `s()`, so it agrees with the fix and disagrees with the bug -- a DOM
 * assertion cannot see a code path the DOM does not use. This gate calls
 * `legacy()` itself, which is the only way to observe it.
 */

const path = require('path');

const { boot } = require('./_i18n_harness.js');

const ASSETS = process.argv[2] || path.join(__dirname, '..', '..', 'site', 'dist', 'assets');
const LOCALES = ['en', 'zh', 'ru'];

// Keys `app.js` resolves through `legacy()`, i.e. the chrome. Chosen because each
// one was visibly wrong on the broken build: the h1, the intro paragraph, the
// sidebar heading, the first filter button and the search box.
const CHROME = [
  ['all', 'the "All shots" filter button'],
  ['categoriesHeading', 'the sidebar heading'],
  ['intro', 'the intro paragraph under the title'],
  ['searchLabel', 'the search input placeholder'],
  ['catCamera', 'a category filter button'],
  ['skip', 'the skip link'],
  ['cards', 'the "Cards" stat label'],
];

// A locale is "speaking" when its strings are not identical to English's. Exact
// equality would be wrong -- brand names and numerals legitimately match -- and
// substring matching would pass on a string that merely contains Latin.
const isEnglish = (s, en) => s === en;

let failures = 0;
let checks = 0;

function ck(ok, label, detail) {
  checks += 1;
  if (ok) {
    console.log(`  ok   ${label}`);
  } else {
    failures += 1;
    console.log(`  FAIL ${label}  -- ${typeof detail === 'function' ? detail() : detail}`);
  }
}

console.log(`i18n runtime :: ${ASSETS}\n`);

const resolved = {};
for (const loc of LOCALES) {
  console.log(`[${loc}]`);
  let I18N;
  try {
    I18N = boot(ASSETS, loc).window.__I18N__;
  } catch (err) {
    ck(false, `${loc}: the runtime boots`, String(err && err.message).slice(0, 160));
    continue;
  }
  ck(!!I18N, `${loc}: window.__I18N__ is exported`,
     () => 'the bundles loaded but nothing assigned window.__I18N__; app.js throws '
         + 'on line 1 and the whole script, including applyLanguage(), never runs');

  if (!I18N) continue;

  const legacy = I18N.legacy();
  const ui = legacy.ui || {};
  const lang = I18N.htmlLang();
  ck(typeof lang === 'string' && /^[-a-zA-Z]+$/.test(lang),
     `${loc}: htmlLang() is a language tag`,
     () => `got ${JSON.stringify(lang)}`);
  ck(I18N.locale === loc,
     `${loc}: locale agrees with the bundle`,
     () => `runtime says ${JSON.stringify(I18N.locale)}; the page loaded `
         + `i18n/${loc}.js`);

  resolved[loc] = { ui, lang };
  console.log('');
}

if (resolved.en && Object.keys(resolved).length > 1) {
  console.log('[chrome keys resolve to this locale, not to en]');
  for (const [key, what] of CHROME) {
    const en = resolved.en.ui[key];
    for (const loc of LOCALES) {
      if (loc === 'en' || !resolved[loc]) continue;
      const v = resolved[loc].ui[key];
      ck(typeof v === 'string' && v.length > 0,
         `${loc}.${key} is present  (${what})`,
         () => `got ${JSON.stringify(v)}; the key is missing from ui.${loc}, so it `
             + `silently falls back`);
      ck(!isEnglish(v, en),
         `${loc}.${key} is not the English string  (${what})`,
         () => `both are ${JSON.stringify(en)} -- the locale never entered the `
             + `fallback chain, which is the bug this file exists for`);
    }
  }
  console.log('');
}

const line = failures === 0
  ? `\n${checks}/${checks} runtime checks passed`
  : `\n${checks - failures}/${checks} runtime checks passed`;
console.log(line);
process.exit(failures ? 1 : 0);