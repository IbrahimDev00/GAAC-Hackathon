#import numpy as np
import mmh3
import xxhash
import cityhash

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
        self.frequencies = {}  # To track actual frequencies for percentile calculation

    def update(self, element):
        if element not in self.frequencies:
            self.frequencies[element] = 0
        self.frequencies[element] += 1  # Update real frequency

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

    def calculate_percentile(self, element):
        """
        Calculate the percentile of an element's frequency.
        """
        if element not in self.frequencies:
            return 0  # Element not in dataset
        freq = self.frequencies[element]
        sorted_frequencies = sorted(self.frequencies.values())
        rank = sorted_frequencies.index(freq) + 1
        percentile = (rank / len(sorted_frequencies)) * 100
        return percentile
