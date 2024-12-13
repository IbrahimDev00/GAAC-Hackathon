import hashlib

class CountMinSketch:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.count_matrix = [[0] * cols for _ in range(rows)]
        self.hash_functions = [hashlib.md5, hashlib.sha1, hashlib.sha256] 

    def update(self, element):
        for i, hash_func in enumerate(self.hash_functions):
            hash_value = int(hash_func(element.encode()).hexdigest(), 16)
            bucket_index = hash_value % self.cols
            self.count_matrix[i][bucket_index] += 1

    def query(self, element):
        min_count = float('inf')
        for i, hash_func in enumerate(self.hash_functions):
            hash_value = int(hash_func(element.encode()).hexdigest(), 16)
            bucket_index = hash_value % self.cols
            min_count = min(min_count, self.count_matrix[i][bucket_index])
        return min_count

# Example usage
cms = CountMinSketch(rows=3, cols=10)
data_stream = ["468529265", "465213832158", "02102358528", "465213832158", "8916571369", "7812303456820", "465213832158"]
for element in data_stream:
    cms.update(element)
print("Frequency of the no is:", cms.query("465213832158"))