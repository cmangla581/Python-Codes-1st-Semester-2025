# Write a python code showint th etuple and person cities 

cities = ("Delhi", "Mumbai", "Chennai", "Kolkata", "Bengaluru")

print("Cities Tuple:", cities) 

print("First City", cities[0])
print("Last City", cities[-1]) 

# Type the whole lit of the city 
print("List of Cities:")
for city in cities:
    print(city) 

# Checking if a city is in tuple or not 

city_to_check = input("Enter the name of the city\n")

if city_to_check in cities: print("City is in tuple")
else: print("Its not in the tuple") 