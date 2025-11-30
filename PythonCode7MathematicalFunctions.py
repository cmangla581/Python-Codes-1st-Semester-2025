import math 

n = int(input("Enter the number "))

cont = int(input("Press 1 for Ceil Function, Press 2 for Square Root, Press 3 for Power, Press 4 for Factorial ")) 

if cont == 1 : print("The ceil function output is ", math.ceil(n))

elif cont == 2 : print("The square root functionoutput is ", math.sqrt(n))

elif cont == 3 :
    a = int(input("Enter a number "))
    print("The power function output is ", math.pow(n,a))

elif cont ==4 : print("The factorial function output is :", math.factorial(n)) 
