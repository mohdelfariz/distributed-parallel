import numpy as np
import multiprocessing as mp
from time import time

print("Number of processors: ", mp.cpu_count())

# Parallelizing using Asynchronous execution type

if __name__ == "__main__":
    # Prepare data (This is the problem statement)
    np.random.RandomState(100)
    arr = np.random.randint(0, 10, size=[200000, 5])
    data = arr.tolist()
    data[:5]
    
    # Non-parallel solution
    def howmany_within_range(row, minimum, maximum):
        # Return how many numbers lie within maximum and minimum in a given row
        count = 0
        for n in row:
            if minimum <= n <= maximum:
                count = count + 1
        return count
    
    results = []
    
    for row in data:
        results.append(howmany_within_range(row, minimum=4, maximum=8))
    
    print(results[:10])
    
    #> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]
