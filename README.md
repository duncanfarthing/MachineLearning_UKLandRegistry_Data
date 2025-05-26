A project to get a better feel for imputing data using MICE (Multiple Imputation by Chained Equations) and Random Forest with a real world dataset. 

I'm working with the UK Land Registry's open dataset for the House Price Index (HPI). One challenge with the data is the presence of real-world gaps in the housing stock across defined geographic regions — for example, areas where there are currently no apartments, making it impossible to generate a price index for that property type. The aim is to accurately predict these missing values. This will enable more comprehensive national analysis and allow for consistent comparison across regions and property types. In the longer term, this approach can support forecasting the investment potential of future residential developments in currently underserved or emerging markets.

Using a Medallion Architecture for the data to help keep things organised and to make transfer to a lakehouse smoother should I want to later

TO-DO
Implement Random Forest
Predict Future index and price values based on trend and passed in scenarios
Further enrichment with GDP, Interest and mortgage rates joind on month and year to improve predictions







