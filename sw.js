const CACHE = 'anamnese-fast-v5';
const ASSETS = ['./', './index.html', './manifest.json', './icon.svg'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Network-first p/ conteúdo que muda (HTML, dados, PDF); cache-first p/ estáticos.
function isFresh(url) {
  return url.includes('painel.html') || url.includes('/recursos/') ||
         url.endsWith('.js') || url.endsWith('.pdf') || url.endsWith('.md') ||
         url.endsWith('.html');
}

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;

  if (req.mode === 'navigate' || isFresh(req.url)) {
    // Rede primeiro; cai no cache só se offline.
    e.respondWith(
      fetch(req).then(r => {
        const copy = r.clone();
        caches.open(CACHE).then(c => c.put(req, copy));
        return r;
      }).catch(() => caches.match(req).then(c => c || caches.match('./index.html')))
    );
    return;
  }

  // Estáticos (icon, manifest): cache-first.
  e.respondWith(
    caches.match(req).then(cached => cached || fetch(req).then(r => {
      const copy = r.clone();
      caches.open(CACHE).then(c => c.put(req, copy));
      return r;
    }).catch(() => cached))
  );
});
