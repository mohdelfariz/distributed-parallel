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

    # Parallel solution using apply_async(), map_async() and starmap_async()
    # This is Pool.apply_async()
    # 1) Edit the function to accept i which is the iteration
    def howmany_within_range2(i, row, minimum, maximum):
        count = 0
        for n in row:
            if minimum <= n <= maximum:
                count = count + 1
        return (i, count)
    
    # 2) Define callback function to collect the output in `results`
    def collect_result(result):
        global results
        results.append(result)

    # 3) Use loop to parallelize
    for i, row in enumerate(data):
        pool.apply_async(howmany_within_range2, args=(i, row, 4, 8), callback=collect_result)

    # 4) Close Pool and let all the processes complete    
    pool.close()
    
    # 5) Postpones the execution of next line of code until all processes in the queue are done.
    pool.join()
    
    # 6) Sort results [OPTIONAL]
    results.sort(key=lambda x: x[0])
    results_final = [r for i, r in results]

    print(results_final[:10])
    #> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]

    # This is Pool.starmap_async()
    # 1) Use the Pool.starmap_async() to the function
    results = pool.starmap_async(howmany_within_range2, [(i, row, 4, 8) for i, row in enumerate(data)]).get()

    # 2) With map, use `howmany_within_range_rowonly` instead
    results = pool.map_async(howmany_within_range_rowonly, [row for row in data]).get()

    # 3) Close the pool
    pool.close()

    print(results[:10])
    #> [3, 1, 4, 4, 4, 2, 1, 1, 3, 3]


    
