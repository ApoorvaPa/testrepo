
import numpy as np
a=np.arange(12)
b=a.reshape(4,3)
print(np.insert(a,-1,12))

print(np.insert(b,-3,12,axis=1))
print(np.insert(b,-4,12,axis=0))