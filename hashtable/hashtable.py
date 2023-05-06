class Hashtable:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def set(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def has(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return True
        return False

    def keys(self):
        keys = set()
        for bucket in self.buckets:
            for k, v in bucket:
                keys.add(k)
        return keys

    def hash(self, key):
        return hash(key) % self.size
