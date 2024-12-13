from cityhash import CityHash64
import cuckoo_filter

def string_hash(input_string: str) -> int:
    hashed_value =  CityHash64(input_string)

#def cuckoo_filter(hashed_value: int):
