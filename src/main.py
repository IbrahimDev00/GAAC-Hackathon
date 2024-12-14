from cuckoo import CuckooFilter
from countmin import CountMinSketch
from test.test import test_large_input  # Importing the test function

# Initialize filters
cf = CuckooFilter(num_of_items=1000000, error_rate=0.1)
cms = CountMinSketch(1000000, 3)

def add_items_cf(input_String: str):
    # check if item present or not, if present update in cms else add in cf and cms to avoid O(k) time complexity
    if cf.lookup(input_String):
        print(f"{input_String} is already in the filter")
        cms.update(input_String)
    else:
        cf.add(input_String)
        cms.update(input_String)

def query_items(input_String: str):
    # check if item present or not in cf, if present query in cms else print not present
    if cf.lookup(input_String):
        print(f"{input_String} is already in the filter")
        print("Frequency of the number is:", cms.query(input_String))
    else:
        print(f"{input_String} is not in the filter")

def main():
    # Running the test function from test.py
    test_large_input()

if __name__ == "__main__":
    main()
