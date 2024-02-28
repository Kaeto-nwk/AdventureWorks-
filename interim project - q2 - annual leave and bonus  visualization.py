import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# Add column names to the dataframe while it's being read
column_names = [ 'Gender', 'VacationHours', 'Bonus', 'SalesYTD']
vacationhrs_df = pd.read_csv(r"C:\Users\kaeto\Documents\DATA ANALYST\PROJECTS\INTERIM PROJECT\interim project - q2 -  final results table.csv", names=column_names)
print(vacationhrs_df)

#plot the scatter graph
plt.scatter(vacationhrs_df['VacationHours'], vacationhrs_df['Bonus'], marker='o', color='teal')

# Calculate equation for trendline
z = np.polyfit(vacationhrs_df['VacationHours'], vacationhrs_df['Bonus'], 1)
p = np.poly1d(z)

# Add trendline to plot
plt.plot(vacationhrs_df['VacationHours'], p(vacationhrs_df['VacationHours']), color='k', linewidth = 1)

# Calculate correlation coefficient 
co_eff = np.corrcoef(vacationhrs_df['VacationHours'], vacationhrs_df['Bonus'])
co_eff1 = 'co-efficient = ' + str(0.38210746) 
print(co_eff)
#print(co_eff1)

#set the scatter plot background color
plt.gca().set_facecolor('whitesmoke') 

# adjusting the label size
plt.tick_params(axis='y', labelsize=10)
plt.tick_params(axis='x', labelsize=10)

# Display correlation coefficient and p-value on the plot
plt.text(1, 6500, co_eff1, fontsize = 9, fontweight = 'bold')

#set the x-axis to start at 0
plt.xlim([0, 40])

# label axis
plt.xlabel('Annual Leave (hrs)', fontsize = 12)
plt.ylabel('Bonus', fontsize = 12)
plt.title('The Relationship Between Annual leave and Bonus', fontsize = 15, fontweight = 'bold')

plt.show()