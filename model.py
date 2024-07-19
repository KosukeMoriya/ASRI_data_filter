
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3D
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data=pd.read_csv('./fishcounts.csv')
print(data)
#this shows nothing since I didn't select any columns

filtered_data=data[data['LocationID'] == 'OZARRMFISHCM01']
filtered_data=filtered_data[filtered_data['CommonName'] == 'Shadow bass']

#narrowing down the dataset

filtered_data.hist('Weight_Grams')
plt.show()

#pie chart for Location ID