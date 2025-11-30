import numpy as np 

arr = np.array([10,20,30,40,50,60,70]) 

print("Original Array")
print(arr) 

print("Iterating through array elements ") 

for element in arr: 
    print(element, end =" ")

print("Array Sicing ")

print("First 3 elements:", arr[:3])
print("Middle elements form 2 to 5", arr[2:6]) 

print("Every second element", arr[::2])
print("Reversed array ",arr [::-1])