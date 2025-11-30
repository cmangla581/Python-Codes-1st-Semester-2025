numbers = [23,45,678,54,12,9] 

multiples_of_5 = list(filter(lambda x : x % 5 ==0, numbers)) 

print("Multiples of 5 are ", multiples_of_5)