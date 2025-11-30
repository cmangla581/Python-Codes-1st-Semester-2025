#  calculate whether a year entered is leap year or not 

y = int(input("Enter a year "))

if y%4 != 0 : print('Not a leap  year')

elif y%4 == 0 and y%100 != 0 : print("A Leap Year") 

elif y%100 ==0 and y%400 != 0 : print("Not a leap Year") 

else: print("A Leap Year") 
