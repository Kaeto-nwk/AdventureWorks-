#What is the relationship between annual leave, bonus and marital status?

import pandas as pd 
from matplotlib import pyplot as plt 
import numpy as np

# add colum names to the dataframe whilst its being read
column_names = ['Gender', 'VacationHours', 'Bonus', 'SalesYTD']
vacationhrs_df = pd.read_csv(r"C:\Users\kaeto\Documents\DATA ANALYST\PROJECTS\INTERIM PROJECT\interim project - q2 -  final results table.csv", names= column_names)

#print(vacationhrs_df)
#print(vacationhrs_df.info())


#show the relationship between annual leave(hrs) ,bonus and Gender 
#create dataframes for Gender : 'M' - male, 'F' - female 

male_vacationhrs_df = vacationhrs_df[vacationhrs_df['Gender'] == 'M']
#print(male_df)
female_vacationhrs_df = vacationhrs_df[vacationhrs_df['Gender'] == 'F']
#print(female_df)

#created scatterplots for each gender
plt.scatter(male_vacationhrs_df['VacationHours'], male_vacationhrs_df['Bonus'], color = 'steelblue', marker= 'd',  label = 'Male')
plt.scatter(female_vacationhrs_df['VacationHours'], female_vacationhrs_df['Bonus'], color = 'hotpink', marker= 'd', label = 'Female')

# Calculate correlation coefficient 
co_eff = np.corrcoef(vacationhrs_df['VacationHours'], vacationhrs_df['Bonus'])
co_eff1 = 'co-efficient = ' + str(0.38210746) 
print(co_eff)
#print(co_eff1)
# Display correlation coefficient and p-value on the plot
plt.text(1, 6500, co_eff1, fontsize = 9, fontweight = 'bold')

#setting the graph background color
plt.gca().set_facecolor('whitesmoke') 

# adjusting the label size
plt.tick_params(axis='y', labelsize = 8)
plt.tick_params(axis='x', labelsize = 8)

plt.xlim([0,40])
plt.xlabel('Annual Leave (hrs)', fontsize = 10)
plt.ylabel('Bonus', fontsize = 10)
plt.title('The Relationship Between Annual Leave, Bonus And Gender', fontsize = 15, fontweight = 'bold')
plt.legend()

plt.show()