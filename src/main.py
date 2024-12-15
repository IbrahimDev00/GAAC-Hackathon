from cuckoo import CuckooFilter
from countmin import CountMinSketch
from test.test import test_large_input  # Importing the test function
from cityhash import CityHash64  # Efficient hash function for CMS


# Initializing filters with tunable parameters
NUM_ITEMS = 1_000_000  # Expected number of items
ERROR_RATE = 0.01  # False positive rate for Cuckoo Filter (1%)
CMS_WIDTH = 10_000  # Width of CountMin Sketch (trade-off: higher width = more space, less error)
CMS_DEPTH = 3  # Depth of CountMin Sketch (more depth = higher accuracy, more space)

cf = CuckooFilter(num_of_items=NUM_ITEMS, error_rate=ERROR_RATE)
cms = CountMinSketch(CMS_WIDTH, CMS_DEPTH)


def string_hash(input_string: str) -> int:
    """Convert a string into a hashed integer for CountMin Sketch."""
    return CityHash64(input_string)


def add_items_cf(input_string: str):
    """
    Add a string to the Cuckoo Filter and update its frequency in CountMin Sketch.
    - Avoids O(k) complexity of directly checking CMS.
    """
    if cf.lookup(input_string):
        # If already in Cuckoo Filter, update frequency in CMS
        cms.update(string_hash(input_string))
        print(f"{input_string} is already in the filter. Frequency updated.")
    else:
        # Otherwise, add to both Cuckoo Filter and CMS
        cf.add(input_string)
        cms.update(string_hash(input_string))
        print(f"{input_string} added to the filter and frequency initialized.")


def query_items(input_string: str):
    """
    Query a string's existence in the Cuckoo Filter and its frequency in CountMin Sketch.
    """
    if cf.lookup(input_string):
        frequency = cms.query(string_hash(input_string))
        print(f"{input_string} exists in the filter. Frequency: {frequency}")
    else:
        print(f"{input_string} does not exist in the filter.")

def main():
    # Running the test function from test.py
    test_large_input()

if __name__ == "__main__":
    main()
