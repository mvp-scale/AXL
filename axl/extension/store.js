// Staging area: captured pages and the files they need, kept in this browser (IndexedDB) until exported, then cleared.
const DB = 'axl-capture', V = 1;
const open = () => new Promise((res, rej) => { const r = indexedDB.open(DB, V);
  r.onupgradeneeded = () => { const d = r.result; d.createObjectStore('pages', { keyPath: 'url' }); d.createObjectStore('assets', { keyPath: 'url' }); };
  r.onsuccess = () => res(r.result); r.onerror = () => rej(r.error); });
const tx = async (store, mode, fn) => { const d = await open(); return new Promise((res, rej) => { const t = d.transaction(store, mode), s = t.objectStore(store); const out = fn(s);
  t.oncomplete = () => res(out && 'result' in out ? out.result : out); t.onerror = () => rej(t.error); }); };
export const put = (store, v) => tx(store, 'readwrite', s => s.put(v));
export const get = (store, k) => tx(store, 'readonly', s => s.get(k));
export const del = (store, k) => tx(store, 'readwrite', s => s.delete(k));
export const all = (store) => tx(store, 'readonly', s => s.getAll());
export const keys = (store) => tx(store, 'readonly', s => s.getAllKeys());
export const clear = async () => { await tx('pages', 'readwrite', s => s.clear()); await tx('assets', 'readwrite', s => s.clear()); };
