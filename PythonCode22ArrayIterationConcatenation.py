import numpy as np 

arr1 = np.array([15,3,9,20,7])
arr2 = np.array([12,8,25,5,18]) 
 
for element in arr1 : print(element, end = " ")
for element in arr2 : print(element, end = " ")

x = sorted(arr1)
y = sorted(arr2)
print(x)
print(y) 

# Concatenation of strings 

arr3 = arr1 +arr2
print(arr3)