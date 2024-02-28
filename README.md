# Adventure Works - Interim Project

## Table of Contents 
[Project Overview](#project-overview)

[Data sources](#data-sources)

[Tools](#tools)

[Data preparation](#data-preparation)

[Exploratory Data Analysis](#exploratory-data-analysis)

[Data Analysis](#data-analysis)

[Results](#results)

[Limitations](#limitations)


## Project Overview 

This project aims to provide insight into a company's customer demographic as well as the employee's effect on the company's revenue. I completed this project within a group of 4 during my data analysis boot camp.

Link to the presentation: https://docs.google.com/presentation/d/1al2H_mAnvzocUQ9SMGTI23cRr0hj3dWjiWP2YlqbpcA/edit#slide=id.g29e572e9e43_2_19


## Data Sources
The data was from Adventure Works 2019 

The data contained information on:
- Employees
- Sales 
- Customers
- Production
- Purchasing 

The data source can be found here:  https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms


## Tools
- SQL - SSMS - Querying 
- Python - matplotlib and pandas - Visualisation  

## Data Preparation 
1. Loaded the database into SMSS
2. Handled missing values
3. Queried the relevant fields and rows to answer questions shown in EDA


## Exploratory Data Analysis 
After exploring and cleaning the data these are the questions we decided to focus on : 

Q1 - What are the regional sales in the best-performing country?

Q2 - What is the relationship between annual leave taken and bonus?

Q3 - What is the relationship between country and revenue?

Q4 - What is the relationship between sick leave and revenue?

Q5 - What is the relationship between store trading duration and revenue? 

Q6 - What is the relationship between the size of the stores, number of employees and revenue?


## Data Analysis 
My focus within the group :  

Q2 - What is the relationship between annual leave taken and bonus?

```
SELECT Gender, VacationHours, sp.Bonus, sp.SalesYTD

FROM [AdventureWorks2019].[HumanResources].[Employee] AS hr_e
JOIN [AdventureWorks2019].[Sales].[SalesPerson] AS sp
   ON hr_e.BusinessEntityID = sp.BusinessEntityID

JOIN [AdventureWorks2019].[Person].[Person] as p
   ON hr_e.BusinessEntityID = p.BusinessEntityID
```   

Q3 - What is the relationship between country and revenue?
```
SELECT sa.[CountryRegionName] AS Country, SUM(sd.[AnnualRevenue]) AS Total_Annual_Revenue
      
 FROM [AdventureWorks2019].[Sales].[vStoreWithAddresses] AS sa
 JOIN [AdventureWorks2019].[Sales].[vStoreWithDemographics] AS sd
    ON sa.BusinessEntityID = sd.BusinessEntityID 
GROUP BY sa.[CountryRegionName] 
ORDER BY Total_Annual_Revenue DESC
```

Q6 - What is the relationship between the size of the stores, number of employees and revenue?
```
SELECT TOP(100) AnnualRevenue, SquareFeet, NumberEmployees
  FROM [AdventureWorks2019].[Sales].[vStoreWithDemographics]
```

## Results
Q2 - What is the relationship between annual leave taken and bonus?

My initial analysis of  the relationship between annual leave and employee bonuses, showed that there was a weak positive correlation between annual leave hours and bonuses. I calculated the correlation co-efficient to be approximately 0.38.

![q2 - relationship between annual leave and bonus](https://github.com/Kaeto-nwk/AdventureWorks-/assets/150389314/dc4662a6-8c2f-4678-bc1e-007251d24f96)

I further analysed this relationship by looking into the gender split and found that men tended to get more bonuses than women.

![q2 - relationship between annual leave, bonus and gender viz](https://github.com/Kaeto-nwk/AdventureWorks-/assets/150389314/3b765143-facf-4819-8023-b82cc4d7fdcc)

Another factor I considered was the sales employees had generated YTD. Interestingly I expected that employees who earned higher bonuses would have higher sales YTD but the data shows that there is not a strict correlation between Sales YTD and Bonuses as some employees who received higher bonuses also generated lower sales YTD.

![q2- relationship between annual leave, bonus and sale ytd](https://github.com/Kaeto-nwk/AdventureWorks-/assets/150389314/f63d4750-0742-4021-9457-ae4b320c0a05)


Q3 - What is the relationship between country and revenue?

The United States had the highest Annual revenue more than 3 times higher than Canada which was the second highest earning country.

![interim project - q3 - countries and revenue graph](https://github.com/Kaeto-nwk/AdventureWorks-/assets/150389314/f6132f8e-6920-4301-be04-ecf369a995db)


Q6 - What is the relationship between the size of the stores, number of employees and revenue?

There is a strong positive relationship between the size of the store and the number of employees as expected. Also, as expected larger stores tend to generate higher annual revenue than smaller stores.

![The relationship Between Size Of Stores, Number Of Employees And Revenue](https://github.com/Kaeto-nwk/AdventureWorks-/assets/150389314/a0945a05-14ee-4647-96b7-501cdce461a5)


## Limitations 

- As the dataset is fictional a few of the values in the fields were repeated which affected the quality of the visualisations.

- The dataset was quite small and didn't provide a large enough sample to work from. 

