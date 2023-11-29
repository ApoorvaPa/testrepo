import numpy as np

a = np.array([[1, 2, np.nan],
              [4, np.nan, 5],
              [np.nan, np.nan, 6]])
print("Array:")
print(a)

# i. Count the number of missing values in 'a'
missing_count = np.isnan(a).sum()
print("\nNumber of missing values:", missing_count)

# ii. Retrieve rows with exactly two missing values
rows_with_two_missing = a[np.sum(np.isnan(a), axis=1) == 2]
print("\nRows with exactly two missing values:")
print(rows_with_two_missing)

# iii. Retrieve columns with at least two missing values
columns_with_missing = a[:, np.sum(np.isnan(a), axis=0) >= 2]
print("\nColumns with at least two missing values:")
print(columns_with_missing)

# iv. Retrieve rows that start with a missing value
rows_starting_with_missing = a[np.isnan(a[:, 0])]
print("\nRows starting with a missing value:")
print(rows_starting_with_missing)
