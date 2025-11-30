# calculate if a number is armstrong number or not 
#  For example An armstorn number si one which is equalt o the sum of the digits to their powers of the same number 
# 153 = 1^1 + 5^5+ 3^3 = 153

n = int(input("Enter the number ")) 

digits = len(str(n))

sumpowers = sum(int(digit) ** digits for digit in(str(n)))

if sumpowers == n : print("The  number is an armstrong number") 
else: print("The number is not an armstrong number")