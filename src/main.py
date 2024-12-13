from cityhash import CityHash64
import cuckoo_filter

cf = cuckoo_filter.CuckooFilter(capacity = 9411764, fingerprint_size = 8, bucket_size = 4, expansion = 2)

def string_hash(input_string: str) -> int:
    hashed_value =  CityHash64(input_string)

def cuckoo_filter(hashed_value: int):
    if hashed_value in cuckoo_filter:
        #call the count-min-sketch
        print('Value exists')
    else:
        # add the value to cuckoo filter
        cf.insert(hashed_value)
        # add the value to count-min-sketch
        # call the count-min-sketch function here
        
        

    