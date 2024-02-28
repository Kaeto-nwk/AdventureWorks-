#q6 - What is the relationship between the size of the stores, number of employees and revenue?
import pandas as pd 
from matplotlib import pyplot as plt 
import numpy as np

column_names = ['AnnualRevenue', 'SquareFeet', 'NumberEmployees']
df = pd.read_csv(r"C:\Users\kaeto\Documents\DATA ANALYST\PROJECTS\INTERIM PROJECT\interim project - question 6.csv", names = column_names)
print(df)

plt.scatter(df['SquareFeet'], df['NumberEmployees'], c = df['AnnualRevenue'], cmap ='Wistia', alpha = 0.7)


#calculate equation for trendline
z = np.polyfit(df['SquareFeet'], df['NumberEmployees'], 1)
p = np.poly1d(z)

#add trendline to plot
plt.plot(df['SquareFeet'], p(df['SquareFeet']), color = 'c', linewidth = 1)

#calc the co-efficient of 
co_eff = np.corrcoef(df['SquareFeet'], df['NumberEmployees'])
print(co_eff)
# to get the text for the co-efficient I copied the co-efficient value and turned it into a string
co_eff1 = 'co-efficient = ' + str(0.97155433)

cbar = plt.colorbar()
cbar.set_label('Annual Revenue', fontsize = 10)
cbar.ax.tick_params(labelsize = 8)

# adjusting the label size
plt.tick_params(axis='y', labelsize = 8)
plt.tick_params(axis='x', labelsize = 8)


plt.xlabel('Store size (sq ft)', fontsize = 10)
plt.ylabel('Number Of Employees', fontsize = 10)

plt.text(10000, 85, co_eff1, fontsize = 8.5, fontweight = 'bold')
plt.title('The relationship Between Size Of Stores, Number Of Employees And Revenue', fontsize = 15)
plt.show()