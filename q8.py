import numpy as np
arr = np.array([[3, 2, 4], [5, 0, 1]])
arr=np.sort(arr)
print(arr)
print(arr[0,2]-arr[1,0])
print(arr[[1,0],[0,2]])
print(arr[:-1])
print(arr[::-1])
print(arr[:-1,[-3,-1]])
print(arr[::-1][:-1])
print(arr[::-1,:-1])