import random
import string
import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from countmin import CountMinSketch
from cuckoo import CuckooFilter

# Initialize filters
cf = CuckooFilter(num_of_items=1000000, error_rate=0.1)
cms = CountMinSketch(1000000, 3)

def add_items_cf(input_String: str):
    # Check if item is present or not; if present, update in CMS, else add to CF and CMS
    if cf.lookup(input_String):
        cms.update(input_String)
    else:
        cf.add(input_String)
        cms.update(input_String)

def calculate_percentile(input_String):
    # Get the frequency of the element from CMS
    frequency = cms.query(input_String)

    # Calculate the total count of all elements across rows in CMS
    total_count = sum(sum(row) for row in cms.count_matrix)

    # Calculate the percentile as (frequency / total_count) * 100
    percentile = (frequency / total_count) * 100 if total_count > 0 else 0
    return percentile

def query_items(input_String: str):
    # Check if item is present in CF; if present, query in CMS, else print not present
    if cf.lookup(input_String):
        frequency = cms.query(input_String)
        percentile = calculate_percentile(input_String)
        print(f"{input_String} is already in the filter")
        print(f"Frequency of the number is: {frequency} and percentile is: {percentile:.2f}%")
    else:
        print(f"{input_String} is not in the filter")

# Generate a list of random strings
def generate_large_input_array(size=1000000, length=10):
    return [''.join(random.choices(string.ascii_lowercase, k=length)) for _ in range(size)]

# Create the large input array
large_input_array = generate_large_input_array()

def test_large_input():
    # Timer for adding items to the filters
    start_time = time.time()

    # Add all items to the filters
    for item in large_input_array:
        add_items_cf(item)

    end_time = time.time()
    print(f"Time taken to add all items: {end_time - start_time:.4f} seconds")

    # Timer for querying items
    start_time = time.time()

    # Query some items to test
    query_items(large_input_array[500000])  # Test with a random item in the middle

    end_time = time.time()
    print(f"Time taken to query items: {end_time - start_time:.4f} seconds")
