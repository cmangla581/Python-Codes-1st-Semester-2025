# To check if the input string is palindrome or not 

def palindrome(n): 
    return str(n) == "".join (reversed(str(n)))

n = int(input("Enter a number "))

if palindrome(n) : print("The number is a palindrome ")

else : print("The number is not a palindroem")

