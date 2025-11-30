file_name = "input.txt" 
with open(file_name, "w") as file : 
    file.write("Hello World")

# Reading from the file 
with open(file_name, "r") as file: 
    content = file.read(3) 

    print("First 3 characters of the file ")
    print(content)