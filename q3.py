import numpy as np

# Create a 1-D NumPy array 'a' with 10 random integers between -10 and 10
a = np.random.randint(-10, 11, size=10)
print("Original Array:", a)

# i. Delete the first and last elements of 'a'
a = np.delete(a, [0, -1])
print("Array after deleting first and last elements:", a)

# ii. Delete the negative elements of 'a'
a = a[a >= 0]
print("Array after deleting negative elements:", a)
