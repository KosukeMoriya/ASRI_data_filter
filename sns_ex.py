#The lecture from the Dr. Han Hu which is teaching the engineering in 
# computer science. Also, this lecture is about the seaborn.
import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('fishcounts.csv')
df = pd.DataFrame(data)

crash_df = sns.load_dataset('car_crashes')

sns.lineplot(data=df,x='x',y='y')


#plt.show()

sns.lineplot(data=df, x='x',y='y')

sns.show()