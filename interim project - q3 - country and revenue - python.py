import pandas as pd 
from matplotlib import pyplot as plt 

df = pd.read_csv(r"C:\Users\kaeto\Documents\DATA ANALYST\PROJECTS\INTERIM PROJECT\interim project - q3 - query table results.csv")
print(df)
colors = ['dodgerblue','grey','grey','grey','grey', 'grey']
plt.bar(df['Country'], df['Total_Annual_Revenue'], color = colors)
plt.xlabel('Country')
plt.ylabel('Total Annual Revenue (millions)')
plt.tick_params(axis='x', labelsize=8)
plt.title('The Relationship Between Revenue And Countries')
plt.show()
