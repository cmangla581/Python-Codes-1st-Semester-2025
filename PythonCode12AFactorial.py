# Calculating the factorial of a number by using loop 

n = int(input("Enter a number\n"))
product = 1 
for i in range(1,n+1):
    product = product * i 

print(f"The factorial of {n} is {product}")