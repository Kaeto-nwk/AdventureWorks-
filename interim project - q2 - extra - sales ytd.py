#What is the relationship between annual leave taken bonus and sales ytd
import pandas as pd 
from matplotlib import pyplot as plt 
import numpy as np

column_names = ['Gender', 'VacationHours', 'Bonus', 'SalesYTD']
vacationhrs2_df = pd.read_csv(r"C:\Users\kaeto\Documents\DATA ANALYST\PROJECTS\INTERIM PROJECT\interim project - q2 -  final results table.csv", names = column_names)


print(vacationhrs2_df)
#print(vacationhrs2_df.info())

#create the scatter plot 
plt.scatter(vacationhrs2_df['VacationHours'], vacationhrs2_df['Bonus'], c = vacationhrs2_df['SalesYTD'], cmap = 'YlOrRd')

#calc the co-efficient 
co_eff = np.corrcoef(vacationhrs2_df['VacationHours'], vacationhrs2_df['Bonus'])
co_eff1 = 'co-efficient = ' + str(0.38210746)
#print(co_eff)

#adding a colormap for the 3rd variable 
cbar = plt.colorbar()
cbar.set_label('Sales YTD')

#set the x-axis to start from zero 
plt.xlim([0,40])

#setting the graph background color
plt.gca().set_facecolor('whitesmoke') 

# adjusting the label size
plt.tick_params(axis='y', labelsize = 8)
plt.tick_params(axis='x', labelsize = 8)

#label the graph 
plt.xlabel('Annual Leave (hrs)', fontsize = 10)
plt.ylabel('Bonus', fontsize = 10 )
plt.text(5, 6500, co_eff1, fontsize = 7, fontweight = 'bold')
plt.title('The Relationship Between Annual leave, Bonus And Sale YTD', fontsize = 15)

plt.show() 

