'''Write a program to show use of library NumPy
1. Create list
2. Add 5 to each element
3. Show data type
'''
import numpy as np

#Integer Array
arr1 = np.array([1,2,3])
print('Elements of the Array : ' + str(arr1))
print('Added 5 to each element : ' + str(arr1+5))
print(np.result_type(arr1))

#Heterogeneous Array
arr2 = np.array([1,'two', 3.5 , 'four'])
print(np.result_type(arr2))
print(type(arr2[0]),type(arr2[1]),type(arr2[2]))

#Matrix
print(np.array([5,6,8,45,12,52]).reshape(2,3))

print(np.matrix([[1,2],[3,4]]))

# Add 2 arrays
arr3 = np.array([25, 56, 12, 85, 34, 75] )
arr4 = np.array([42, 3, 86, 32, 856, 46])
print(arr3+arr4)

mat1 = np.matrix(arr3)
print(mat1)

