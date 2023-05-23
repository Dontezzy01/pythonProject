import numpy as np

Arr=np.array([12,21,13,13,34,98,90])
print(max(Arr))


# Matrices in a array
Arr1=np.array([
    [9,8,7,4],
     [4,2,9,81]
            ])
Arr2= Arr1.flatten()
Arr3 = Arr2.reshape(2,4)
print(Arr2)
print(Arr3)
print(Arr1.size)
print(Arr1.shape)
print(Arr1.dtype)

#from numpy import*

#m = matrix("1,2,3,4 : 7,8,9,0")

#print(m)