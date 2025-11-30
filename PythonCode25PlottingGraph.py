import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10]) 

plt.plot(x,y, marker = 'o', color ='green', linestyle = '-', label = 'y=2x') 

plt.title("Single Line Graph using Matplotlib")

plt.xlabel("X Axis Coordinates")
plt.ylabel('Y Axis Coordinates')
plt.legend()
plt.show()