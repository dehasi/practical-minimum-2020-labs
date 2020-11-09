class Service:

    def __init__(self, cache, database):
        self.cache = cache
        self.database = database

    def get(self, key):
        if self.cache.exists(key):
            return self.cache.get(key)

        value = self.database.get(key)
        if value is not None:
            self.cache.put(key, value)
        return value

    def put(self, key, value):
        self.database.put(key, value)

    def delete(self, key):
        self.cache.delete(key)
        self.database.delete(key)
