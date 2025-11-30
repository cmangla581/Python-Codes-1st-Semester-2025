file_name = 'input.txt' 
# Writing from the file 
with open(file_name, "w") as file : file.write("Computer Science")

# Reading from the file 
with open(file_name, "r") as file : 
    content = file.read() 

print("Content of the file")
print(content) 