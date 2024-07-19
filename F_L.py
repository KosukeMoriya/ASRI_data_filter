'''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'fishcounts.csv'
data = pd.read_csv(file_path, usecols=['TotalLength_Millimeters','pH'])
#ColumX and ColumY should be replaced with the real clomun name in the file. 

data.rename(columns={'TotalLength_Millimeters': 'x', 'pH': 'y'}, inplace=True)
#Create DataFrame columns={'ColumnX': 'x', 'ColumnY': 'y'} to have consistency for later! 
#Q. What is inplace=True? 
#A. 

plt.scatter(data['x'], data['y'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot of x vs y')
plt.show()

#Ask how to debug on 6/14
#I want to use two files with the same column. Two files are fishcounts.csv and
#reachmeasurements.csv. The column is the oxyzenperliter in the 
#reachmeasuremetns.csv. The other column is the weight of the fish. I don't 
#know how to get each data from each file. Also, I want to learn how to clean the
#data from the columns such as oxyzenperliter having outliner value. 

#I want to know how to use colab as well. 

'''