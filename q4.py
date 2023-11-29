import numpy as np

a = np.arange(25).reshape(5, 5)
print("Original Array:")
print(a)

# i. Delete the first and last columns from 'a'
a1 = np.delete(a, [0, -1], axis=1)
print("\nArray after deleting first and last columns:",a1)
print(a1)

# ii. Delete the first and last rows from 'a'
a2 = np.delete(a, [0, -1], axis=0)
print("\nArray after deleting first and last rows:")
print(a2)
