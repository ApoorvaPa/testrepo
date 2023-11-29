import numpy as np

a = np.random.randint(-20, 20, size=20).reshape(5, 4)
print("Array:")
print(a)

# i. Retrieve rows that start with a negative integer
negative_start_rows = a[a[:, 0] < 0]
print("\nRows starting with a negative integer:")
print(negative_start_rows)

# ii. Count the number of negative integers in 'a'
negative_count = np.sum(a < 0)
print("\nNumber of negative integers:", negative_count)

# iii. Retrieve rows with exactly two negative integers
rows_with_two_negatives = a[np.sum(a < 0, axis=1) == 2]
print("\nRows with exactly two negative integers:")
print(rows_with_two_negatives)

# iv. Retrieve column with the largest integer
column_with_largest_int = a[:, np.argmax(a.max(axis=0))]
print("\nColumn with the largest integer:")
print(column_with_largest_int)
