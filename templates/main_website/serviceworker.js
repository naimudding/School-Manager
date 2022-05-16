
var staticCacheName = 'schoolmanager';

var add_list = ["/home", '/offline_page']


self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll(add_list);
    })
  );
});

self.addEventListener('activate', function(event) {
  event.waitUntil(
  );
});


self.addEventListener('fetch', function(event) {

  event.respondWith(fromNetwork(event.request, 400).catch(function () {
    return fromCache(event.request);
    }));

  event.waitUntil(caches.open(staticCacheName)
  .then(cache => fetch(event.request)
    .then(response =>{
        if(url.includes('media/') | url.includes('static/')){
          cache.put(event.request, response)
          }
        }
     )));
});

function fromNetwork(request, timeout) {
  return new Promise(function (fulfill, reject) {
    // var timeoutId = setTimeout(reject, 000);

    fetch(request).then(function (response) {
      // clearTimeout(timeoutId);
      fulfill(response);

    }, reject);
  });
}

function fromCache(request) {
  return caches.open(staticCacheName).then(function (cache) {
    var requestUrl = new URL(request.url);
    if(requestUrl.pathname == '' | requestUrl.pathname == '/'){
      return cache.match('/company')
    }
    else {
      return cache.match(request).then(function (matching) {
        return matching || cache.match('/offline_page')
      })
    }
  });
}


