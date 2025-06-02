const cacheName = "nasz-prad-cache-v1";
const filesToCache = [
  "/agent.html",
  "/callcenter.html",
  "/logo.jpg",
  "/logo-192x192.png",
  "/manifest.json"
];

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(cacheName).then(cache => {
      return cache.addAll(filesToCache);
    })
  );
});

self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});