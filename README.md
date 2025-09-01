# Moroccan-energy-consumption

This is an overview of an analysis conducted on an energy-related dataset focusing on electricity consumption patterns in Morocco. The analysis explores various aspects of the dataset, including seasonal patterns, correlations between different variables, and the transformation of the date column into a time series format using pandas.

Key Findings:

The findings revealed temperature as the primary environmental factor since it had a low to moderate influence on electricity consumption patterns compared to humidity and wind speed. Its correlation with power consumption was 0.45 for Zone 3, while Zone 1 and Zone 2 had 0.40 and 0.34, respectively. This indicated that higher temperatures often led to increased electricity consumption, which was evident in the summer months of July and August. 

The findings also show peak demand at 8 PM, indicating a period when many people are home using power-consuming appliances and off-peak hours between 5 AM and 9 AM, indicating a period when people are away from home or are at work. 

The analysis also highlights the supplementary role of solar power and wind energy in meeting power demands, alongside the existing on-grid efforts. Additionally, it outlines the data preprocessing steps undertaken to ensure data quality and integrity before conducting the analysis.

Using Python's data science libraries, I preprocessed the data by scaling, encoding, and transforming the data to prepare it for the modelling stage.

The machine learning models were excellent at handling nonlinear relationships between the variables, and based on the performance metrics of the three models used, namely XGBoost, Decision Trees and Random Forest, XGBoost merged as the dominant model. It had an R² score of 0.9662 in Zone 1, 0.9652 in Zone 2 and 0.9780 in Zone 3. It also had the least errors with an MAE score of 907.86, 677.45 and 603.00 in Zone 1, 2 and 3, respectively, and an RMSE score of 1257.97 in Zone 1, 932.63 in Zone 2 and 859.92 in Zone 3 further confirming its effectiveness and high accuracy in capturing electricity consumption across multiple zones. 

![alt text](https://github.com/kahumawalter/moroccan-energy-consumption/blob/main/heatmap.png)
