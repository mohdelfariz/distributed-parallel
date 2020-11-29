# Assignment-2
# (a) Write a Pandas program to add, subtract, multiple, divide and compare two Pandas Series.
# Sample Series: [1, 3, 5, 7, 9] & [2, 4, 6, 8, 10]

import numpy as np
import pandas as pd

sample1 = pd.Series([1, 3, 5, 7, 9])
sample2 = pd.Series([2, 4, 6, 8, 10])

print("Answer for question (a)")
sample = sample1 + sample2
print("\n")
print("Addition of two Pandas Series:")
print(sample)

print("\n")
print("Subtraction of two Pandas Series:")
sample = sample1 - sample2
print(sample)

print("\n")
print("Multiplication of two Pandas Series:")
sample = sample1 * sample2
print(sample)

print("\n")
print("Division of two Pandas Series:")
sample = sample1 / sample2
print(sample)


# (b) Write a Pandas program to convert a NumPy array to a Pandas series.
# Sample NumPy array: D = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("\n")
print("Answer for Question (b)")
np_array = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("NumPy array:")
print(np_array)
print("\n")

new_series = pd.Series(np_array)
print("Converted to Pandas Series:")
print(new_series)
