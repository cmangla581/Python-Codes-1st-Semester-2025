# Here also we plot a histogram based on th data of age, weight andbmi 

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# Creation of the data  
data = {
    "Age" : [20, 25, 30,35,40], 
    "Weight" : [60, 65, 70, 75, 80], 
    "BMI" : [22.5, 24.1, 25.0, 26.3,27.5]
}
df = pd.DataFrame(data)
print(df) 

# Creating the csv file in it 
df.to_csv("heath_data.csv", index = False)
print("CSV file dreated successfully") 

# Reading the File  
df_read = pd.read_csv('D:\Coding\Python Practicals Practice\heath_data.csv')
print(df_read) 

# Plotting of the histogram 
plt.hist(data["BMI"]) 
plt.title("BMI Distribution")
plt.xlabel("BMI")
plt.ylabel("Frequency")

plt.grid(True)
plt.legend()
plt.show() 

sns.pairplot(df, hue='BMI')
plt.show()