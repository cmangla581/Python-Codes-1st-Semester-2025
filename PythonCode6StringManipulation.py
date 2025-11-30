'''
 Here we will use string manipulation to find the operation like the : 
 Find()
 Upper()
 Length()
 Max() and Min()
 Fetching a Specific Content by inexing 
 ''' 

string = input("Enter the string ")

cont = int(input("Press 1 for Find, 2 for Upper, 3 for length, 4 for Maximum, 5 for Minimum and 6 for fetching "))

if cont ==1 : 
    a = input("Enter the substring to find ") 
    print("The index of the substring is: ", string.find(a)) # Find the location of  string of a  

elif cont == 2 : 
    print("The string in upper case is; ", string.upper()) 

elif cont == 3 : 
    print("The length of the string is:", len(string)) 

elif cont ==4 : 
    print(max(string)) 

elif cont ==5 : 
    print(min(string)) 

elif cont ==6 : 
    i1 = int(input("Enter the first index "))
    i2 = int(input("ENter the second index "))
    print(string[i1:i2])


