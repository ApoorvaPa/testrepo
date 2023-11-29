import numpy as np

arr = np.random.randint(-15, 21, size=10)
print(arr)

negative_count = np.sum(arr < 0)
print("Number of negative integers:", negative_count)


subarr1 = np.sum((arr<5)&(arr>-5))
print("No. of integers between -5 and 5 are:", subarr1)


subarr2 = np.sum(arr%2==0)
print("No. of even integers", subarr2)

arr[arr < 0] = 0
print("Array after replacing negatives with 0:", arr)