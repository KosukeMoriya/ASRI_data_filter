#This file shows how to show the column's value from dataset. 
import pandas as pd


data=pd.read_csv('fishcounts.csv')
numberofrainbow = data['ParkName'].value_counts().head()
print(numberofrainbow)




