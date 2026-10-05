/**
 * A DOM shim just large enough to execute the built i18n runtime under node.
 *
 * The runtime is a browser IIFE that reads `global.__I18N_DATA__` and reaches for
 * `document` in `apply()` and `mountSwitcher()`. Nothing else is needed, because
 * the question this harness answers -- "does the lookup return the page's
 * language?" -- is answered before any of that.
 *
 * Loaded with `vm.runInNewContext` rather than `require`, so the script's own
 * scope is the context's global: `window.__I18N__ = ...` has to land where the
 * page would see it, exactly as it does in a browser.
 */

const fs = require('fs');
const vm = require('vm');

function makeDocument() {
  const listeners = {};
  const makeEl = (tag) => ({
    tagName: (tag || 'div').toUpperCase(),
    dataset: {},
    style: {},
    children: [],
    attributes: {},
    textContent: '',
    innerHTML: '',
    classList: { add() {}, remove() {}, contains() { return false; }, toggle() {} },
    setAttribute(k, v) { this.attributes[k] = String(v); },
    getAttribute(k) { return this.attributes[k] ?? null; },
    removeAttribute(k) { delete this.attributes[k]; },
    hasAttribute(k) { return k in this.attributes; },
    appendChild(c) { this.children.push(c); return c; },
    append(...c) { this.children.push(...c); },
    addEventListener(t, fn) { (listeners[t] ||= []).push(fn); },
    removeEventListener() {},
    focus() {},
    click() {},
    querySelector() { return null; },
    querySelectorAll() { return []; },
    closest() { return null; },
    contains() { return false; },
    getBoundingClientRect() { return { top: 0, left: 0, width: 0, height: 0 }; },
  });
  return {
    documentElement: makeEl('html'),
    body: makeEl('body'),
    head: makeEl('head'),
    createElement: makeEl,
    createTextNode: (t) => ({ nodeType: 3, textContent: t }),
    createDocumentFragment: () => makeEl('fragment'),
    querySelector: () => null,
    querySelectorAll: () => [],
    getElementById: () => null,
    addEventListener: (t, fn) => { (listeners[t] ||= []).push(fn); },
    removeEventListener: () => {},
    readyState: 'complete',
    location: { pathname: '/', hash: '', search: '', href: 'http://x/' },
    documentURI: 'http://x/',
  };
}

/**
 * Load `assets/i18n/<locale>.js` then `assets/i18n.js` into one fresh context and
 * return the resulting `window`.
 */
function boot(assetsDir, locale) {
  const sandbox = {
    console,
    setTimeout,
    clearTimeout,
    setInterval,
    clearInterval,
    document: makeDocument(),
    navigator: { language: locale, languages: [locale] },
    location: { pathname: `/${locale}/library.html`, hash: '', search: '' },
    localStorage: {
      _v: {},
      getItem(k) { return k in this._v ? this._v[k] : null; },
      setItem(k, v) { this._v[k] = String(v); },
      removeItem(k) { delete this._v[k]; },
    },
    matchMedia: () => ({ matches: false, addEventListener() {}, addListener() {} }),
    fetch: () => Promise.reject(new Error('offline')),
    // The runtime registers a DOM-ready listener and may run immediately when the
    // document is already complete. Both paths must exist or it throws before a
    // single string is resolved -- which is why the harness asserts the runtime
    // *boots* separately from what it returns.
    addEventListener: () => {},
    removeEventListener: () => {},
    dispatchEvent: () => true,
    requestAnimationFrame: (fn) => { fn(0); return 0; },
    cancelAnimationFrame: () => {},
    getComputedStyle: () => ({ getPropertyValue: () => '' }),
    innerWidth: 1440,
    innerHeight: 900,
    scrollY: 0,
    pageYOffset: 0,
    Event: class Event { constructor(type) { this.type = type; } },
    CustomEvent: class CustomEvent {
      constructor(type, init) { this.type = type; this.detail = (init || {}).detail; }
    },
  };
  sandbox.window = sandbox;
  sandbox.globalThis = sandbox;
  sandbox.self = sandbox;
  vm.createContext(sandbox);

  for (const f of [`i18n/${locale}.js`, 'i18n.js']) {
    const src = fs.readFileSync(`${assetsDir}/${f}`, 'utf8');
    vm.runInContext(src, sandbox, { filename: f });
  }
  return sandbox;
}

module.exports = { boot, makeDocument };