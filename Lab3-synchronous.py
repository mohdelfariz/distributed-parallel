# Lab3-Synchronous
import numpy as np
import multiprocessing as mp
from time import time

print("Number of processors: ", mp.cpu_count())

# Parallelizing using Synchronous execution type

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
    
    # Parallel solution (pool.apply(), pool.map() and pool.starmap()

    # This is Pool.apply()
    # 1) Initialize multiprocessing.Pool()
    pool = mp.Pool(mp.cpu_count())

    # 2) pool.apply() the defined function howmany_within_range()
    results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data]

    # 3) Close the pool
    pool.close()

    print(results[:10])
    #> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]
    
    # This is Pool.map()
    # 1) Edit the function of howmany_within_range
    def howmany_within_range_rowonly(row, minimum=4, maximum=8):
        count = 0
        for n in row:
            if minimum <= n <= maximum:
                count = count + 1
        return count
    
    pool = mp.Pool(mp.cpu_count())
    
   
    results = pool.map(howmany_within_range_rowonly, [row for row in data])
    
    # 3) Close the pool
    pool.close()
    
    print(results[:10])
    #> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]
    
    # This is Pool.starmap()
    pool = mp.Pool(mp.cpu_count())

     # 1) pool.map() the defined function howmany_within_range()
    results = pool.starmap(howmany_within_range, [(row, 4, 8) for row in data])

    # 2) Close the pool
    pool.close()

    print(results[:10])
    #> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]
