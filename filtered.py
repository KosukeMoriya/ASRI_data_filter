#This file shows how to fileter the data in the dataframe. Also, this file
#shows how to get the desired data column in a different file.
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

filtered_data=pd.read_csv('reachmeasurements.csv')
#Create filter
filtered_data = filtered_data[filtered_data.DissolvedOxygen_MilligramsPerLiter 
                              != -999]
filtered_data = filtered_data[['ParkName',
                               "DissolvedOxygen_MilligramsPerLiter"]]
#Select the columns from the dataframe based on the park name and DO_m/L
grp = filtered_data.groupby('ParkName')[['DissolvedOxygen_MilligramsPerLiter']
                                        ].mean().round(2)
#get the mean value

filtered_data_counts = pd.read_csv("fishcounts.csv")
filtered_data_counts = filtered_data_counts
[filtered_data_counts.TotalLength_Millimeters != -999]
filtered_data_counts = filtered_data_counts[['ParkName',"TotalLength_Millimeters"]]
grp_counts = filtered_data_counts.groupby('ParkName')[['TotalLength_Millimeters']].count()

#Filter the data based on the TotalLength_Millimeters which is the dataframe.
#Get the count based on the ParkName since the dataframe's raw shows the number of fish.
column_x = grp["DissolvedOxygen_MilligramsPerLiter"]
column_y = grp_counts['TotalLength_Millimeters']

combined_data = pd.DataFrame({'DissolvedOxygen_MilligramsPerLiter': column_x, 'TotalLength_Millimeters': column_y})

sns.barplot(x="DissolvedOxygen_MilligramsPerLiter", y="TotalLength_Millimeters", data=combined_data)
plt.show()