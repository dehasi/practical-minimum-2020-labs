class RedisRepository:
    def __init__(self, redis_client):
        self.redis_client = redis_client

    def exists(self, key):
        return self.redis_client.exists(key)

    def get(self, key):
        return self.redis_client.get(key)

    def put(self, key, value):
        return self.redis_client.set(key, value)

    def delete(self, key):
        return self.redis_client.delete(key)

