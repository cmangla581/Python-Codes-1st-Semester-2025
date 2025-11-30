''' Here we ccreate 2 lit and do the following opertions 
Add, Compare, Find no. of elements, sort the elemts, reverse contents of list ''' 

list1 =[10,20,20]
list2 = [10,20,30, 90] 

# Adding the elements in list 
list1.append(40)
list2.append(50)

print(list1)
print(list2)

# Comparint of the lists 
if list1 == list2 : 
    print("Bth lists have same content")
else : print("Both lists have different content")

# Find the length of the list 
print(len(list1))
print(len(list2)) 

# Sorting the leements of the list 
list1_sorted = sorted(list1) 
print("The list with sorted elements is:", list1_sorted)
list2_sorted = sorted(list2) 
print("The list with sorted elements is:", list2_sorted)

# Reverse the lements of the list 
list1_reversed = list1[::-1]
print(list1_reversed)

list2_reversed = list2[::-1]
print(list2_reversed)


