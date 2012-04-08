from dogpile.cache.region import register_backend

register_backend("dogpile.cache.dbm", "dogpile.cache.backends.file", "DBMBackend")
register_backend("dogpile.cache.pylibmc", "dogpile.cache.backends.memcached", "PylibmcBackend")
register_backend("dogpile.cache.bmemcached", "dogpile.cache.backends.memcached", "BMemcachedBackend")
register_backend("dogpile.cache.memcached", "dogpile.cache.backends.memcached", "MemcachedBackend")
register_backend("dogpile.cache.memory", "dogpile.cache.backends.memory", "MemoryBackend")
