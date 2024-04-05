# Moroccan-energy-consumption

This is an overview of an analysis conducted on an energy-related dataset focusing on electricity consumption patterns in Morocco. The analysis explores various aspects of the dataset, including seasonal patterns, correlations between different variables, and the transformation of the date column into a time series format using pandas.

Key Findings:

Peak electricity consumption occurs at 8 pm every day, with the highest levels observed in July and August.
Zone 1 exhibits the highest power consumption, followed by Zone 2 and Zone 3.
Strong positive correlations exist between power consumption in different zones, with weaker correlations between environmental factors such as temperature, humidity, and wind speed.

The analysis also highlights the supplementary role of solar power and wind energy in meeting power demands, alongside the existing on-grid efforts. Additionally, it outlines the data preprocessing steps undertaken to ensure data quality and integrity before conducting the analysis.

Using Python's data science libraries, I preprocessed the data by scaling, encoding, and transforming the data to prepare it for the modelling stage.

After testing with different regression models, I zeroed down on the Random Forest Regression model which I finely tuned and its performance was nothing short of extraordinary, with R-squared scores of 0.9783, 0.9782, and 0.9863 for Zones 1, 2, and 3, respectively, painting a vivid picture of the model's uncanny ability to predict electricity consumption patterns.

![alt text](https://github.com/kahumawalter/moroccan-energy-consumption/blob/main/heatmap.png)
