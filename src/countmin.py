import cityhash
import mmh3
import xxhash
import random
import time

class CountMinSketch:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.count_matrix = [[0] * cols for _ in range(rows)]
        self.hash_functions = [
            lambda x: int(xxhash.xxh64(x).hexdigest(), 16),
            lambda x: abs(mmh3.hash(x)),
            lambda x: abs(cityhash.CityHash64(x))
        ]

    def update(self, element):
        for i, hash_func in enumerate(self.hash_functions):
            hash_value = hash_func(element)
            bucket_index = hash_value % self.cols
            self.count_matrix[i][bucket_index] += 1

    def query(self, element):
        min_count = float('inf')
        for i, hash_func in enumerate(self.hash_functions):
            hash_value = hash_func(element)
            bucket_index = hash_value % self.cols
            min_count = min(min_count, self.count_matrix[i][bucket_index])
        return min_count

# Main execution and testing
if __name__ == "__main__":
    # # Example usage
    # cms = CountMinSketch(rows=3, cols=10)
    # data_stream = ["468529265", "465213832158", "02102358528", "465213832158", "8916571369", "7812303456820", "465213832158"]
    # for element in data_stream:
    #     cms.update(element)

    # print("Frequency of the number is:", cms.query("465213832158"))

    # Performance test with large dataset
    print("\nPerformance Test")

    # Initialize CountMinSketch with larger size
    cms = CountMinSketch(rows=3, cols=10_000)

    # Generate 1 millionp numbers and feed into the algo
    def generate_large_numeric_dataset(size, number_range=(0, 1_000_000)):
        return [str(random.randint(*number_range)) for _ in range(size)]

    dataset = generate_large_numeric_dataset(1_000_000)

    # Measuring the update time
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
