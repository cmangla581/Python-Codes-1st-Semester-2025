# Creatioj of the csv file 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

data = { 
    "Age" : [20, 25,30,35,40],
    "Weight" :[60,65,70,75,80],
    "BMI" : [22.5, 24.1, 25.0, 26.3,27.5]
}

df= pd.DataFrame(data)
print(df) 

# Saving to csv file 
df.to_csv("health_data.csv", index=False)
print("CSV File 'health_data.csv' created successfully ") 

# Reading the csv file 
df_read = pd.read_csv('D:\Coding\Python Practicals Practice\health_data.csv')
print("Contents of the File")
print(df_read)

# Plotting of the graph 
plt.plot(df_read['Age'], df_read['Weight'], marker ='o', label = 'weight')
plt.plot(df_read['Age'], df_read['BMI'], marker ='o', label = 'BMI') 

plt.title("Age vs Weight and BMI")
plt.xlabel("Age")
plt.ylabel("Values")
plt.legend()
plt.grid(True)
plt.show()

sns.pairplot(df_read, hue='BMI')
plt.show()