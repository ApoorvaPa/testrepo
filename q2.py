import numpy as np

a = np.array([1,2,2,3,3,3,4,4,4,4])
print(a)
unique=np.unique(a)
print(unique)
duplicate_count = len(a) - len(unique)
print("Number of duplicate elements:", duplicate_count)
