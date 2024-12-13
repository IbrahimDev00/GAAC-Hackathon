import random 
from cityhash import CityHash64
import numpy as np

def cuckoo_fil(num_of_items, error_rate, itemsAdd, itemsLookup, itemsDelete, maxKicks=500):
    fingerprint = 8
    num_of_buckets = np.ceil((num_of_items / error_rate) / 2)       #formula
    bucketSize = 4

buckets = [[] for _ in range(num_of_buckets)]            #empty buckets initialization

def hashIndex(hashValue):    #mapping hash value to bucket index
        return hashValue % int(num_of_buckets)

def altIndex(hashValue, index):     #calculating alternate bucket index
        return (index ^ hashValue) % int(num_of_buckets)

def add(item):          #adding item to filter
        hashValue = CityHash64(item)
        index = hashIndex(hashValue)
        altIndexVal = altIndex(hashValue, index)

#one of the two buckets are inserted 
        for i in (index, altIndexVal):
            if len(buckets[i]) < bucketSize:
                buckets[i].append(hashValue)
                return True
        
        currentIndex = random.choice([index, altIndexVal])
        for _ in range(maxKicks):
            evictItem = random.choice(buckets[currentIndex])
            buckets[currentIndex].remove(evictItem)
            buckets[currentIndex].append(hashValue)
            hashValue = evictItem
            currentIndex = altIndex(hashValue, currentIndex)
            if len(buckets[currentIndex]) < bucketSize:
                buckets[currentIndex].append(hashValue)
                return True
        return False  
def lookup(item):
        hashValue = CityHash64(item)
        index = hashIndex(hashValue)
        altIndexVal = altIndex(hashValue, index)
        return hashValue in buckets[index] or hashValue in buckets[altIndexVal]

# add items
for item in itemsAdd:
        add(item)

# lookup items
lookupResults = {item: lookup(item) for item in itemsLookup}

