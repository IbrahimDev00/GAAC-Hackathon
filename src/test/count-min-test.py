# src/test/test_countmin.py
from ..countmin import CountMinSketch

import random
import time

# Initialize CountMinSketch
cms = CountMinSketch(rows=3, cols=10_000)

# Generate and feed numbers
def generate_large_numeric_dataset(size, number_range=(0, 1_000_000)):
    return [random.randint(*number_range) for _ in range(size)]

dataset = generate_large_numeric_dataset(1_000_000)

start_time = time.time()
for number in dataset:
    cms.update(number)
end_time = time.time()

print(f"Time taken to update with {len(dataset)} numbers: {end_time - start_time:.2f} seconds")

# Query test
test_numbers = random.sample(dataset, 1000)
start_time = time.time()
query_results = [cms.query(number) for number in test_numbers]
end_time = time.time()

print(f"Time taken to query 1000 numbers: {end_time - start_time:.2f} seconds")
