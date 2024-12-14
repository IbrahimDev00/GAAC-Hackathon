import random 
from cityhash import CityHash64
import numpy as np

class CuckooFilter:
    def __init__(self, num_of_items, error_rate, fingerprint=8, bucket_size=4, max_kicks=500):
        self.fingerprint = fingerprint
        self.num_of_buckets = int(np.ceil((num_of_items / error_rate) / 2))
        self.bucket_size = bucket_size
        self.max_kicks = max_kicks
        self.buckets = [[] for _ in range(self.num_of_buckets)]

    def hash_index(self, hash_value):
        return hash_value % self.num_of_buckets

    def alt_index(self, hash_value, index):
        return (index ^ hash_value) % self.num_of_buckets

    def add(self, item):
        hash_value = CityHash64(item)
        index = self.hash_index(hash_value)
        alt_index_val = self.alt_index(hash_value, index)

        # Try primary locations
        for i in (index, alt_index_val):
            if len(self.buckets[i]) < self.bucket_size:
                self.buckets[i].append(hash_value)
                return True

        # Cuckoo kicking
        current_index = random.choice([index, alt_index_val])
        for _ in range(self.max_kicks):
            if len(self.buckets[current_index]) < self.bucket_size:
                self.buckets[current_index].append(hash_value)
                return True
            evict_item = random.choice(self.buckets[current_index])
            self.buckets[current_index].remove(evict_item)
            self.buckets[current_index].append(hash_value)
            hash_value = evict_item
            current_index = self.alt_index(hash_value, current_index)
        return False

    def lookup(self, item):
        hash_value = CityHash64(item)
        index = self.hash_index(hash_value)
        alt_index_val = self.alt_index(hash_value, index)
        return hash_value in self.buckets[index] or hash_value in self.buckets[alt_index_val]