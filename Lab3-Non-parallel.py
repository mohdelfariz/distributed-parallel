import multiprocessing as mp
import numpy as np

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[10000, 5])
data = arr.tolist()
data[:5]

# Solution without parallelization
def howmany_within_range_rowonly(row, minimum=4, maximum=8):
    """ Returns how many numbers lie within 'maximum' and 'minimum' in a given 'row'"""

    count = 0

    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

pool = mp.Pool(mp.cpu_count())

results = pool.map(howmany_within_range_rowonly, [row for row in data])

pool.close()

print(results[:10])

# The results for the first 10 row which means
# 2 number within the range in row 1
#> [2, 2, 2, 3, 3, 3, 3, 4, 2, 1]

