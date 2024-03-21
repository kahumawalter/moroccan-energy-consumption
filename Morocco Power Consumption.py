#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


# Loading dataset 

df = pd.read_csv('downloads/electricity+consumption/powerconsumption.csv')
df.head()


# In[3]:


# Checking for data and missing values
df.info()


# In[4]:


#Changing date column to a time series
df['Datetime'] = pd.to_datetime(df['Datetime'])


# In[40]:


#Creating new columns out of the date time column

df['Hour'] = df['Datetime'].dt.hour
df['Month'] = df['Datetime'].dt.month_name()
df['Week Day'] = df['Datetime'].dt.day_name()

df.head()


# In[86]:




# Increase the size of the plot
plt.figure(figsize=(10, 8))

# Create the line plot
sns.lineplot(data=df, x='Month', y='PowerConsumption_Zone1', label= 'Zone1')
sns.lineplot(data=df, x='Month', y='PowerConsumption_Zone2',label='Zone 2')
sns.lineplot(data=df, x='Month', y='PowerConsumption_Zone3', label='Zone 3')

# Set title and labels
plt.title('Power Consumption in Zones According to Months')
plt.xlabel('Month')
plt.ylabel('Power Consumption')
plt.xticks(rotation=45)


# Add grid lines
plt.grid(True, linestyle='--', alpha=0.9)

# Tighten layout
plt.tight_layout()

# Show the plot
plt.show()


# Based on the graph, the highest power consumption occurred predominantly in August for Zones 1 and 2, while Zone 3 saw its peak in July. Conversely, the lowest power utilization was observed in November and December for Zone 1, April for Zone 2, and December for Zone 3.
# 
# Moreover, the graph illustrates that Zone 1 exhibited the highest power consumption, ranging between 30,000 to 35,000 kWh, followed by Zone 2, with consumption levels ranging from 18,000 to 24,000 kWh. Zone 3 registered the lowest consumption, ranging from 12,000 to 26,000 kWh.

# In[58]:


# Increase the size of the plot
plt.figure(figsize=(10, 8))

# Create the line plot
sns.lineplot(data=df, x='Hour', y='PowerConsumption_Zone1', label= 'Zone1')
sns.lineplot(data=df, x='Hour', y='PowerConsumption_Zone2',label='Zone 2')
sns.lineplot(data=df, x='Hour', y='PowerConsumption_Zone3', label='Zone 3')

# Set title and labels
plt.title('Power Consumption According to Time')
plt.xlabel('Time')
plt.ylabel('Power Consumption')


# Add grid lines
plt.grid(True, linestyle='--', alpha=0.9)

# Tighten layout
plt.tight_layout()

# Show the plot
plt.show()


# As per the data presented in the graph, the peak consumption of power consistently occurs at 20:00 hours, while the lowest usage is consistently observed between 5:00 and 7:00 in the morning across all zones.

# In[57]:


# Increase the size of the plot
plt.figure(figsize=(10, 8))

# Create the line plot
sns.lineplot(data=df, x='Week Day', y='PowerConsumption_Zone1', label= 'Zone1')
sns.lineplot(data=df, x='Week Day', y='PowerConsumption_Zone2',label='Zone 2')
sns.lineplot(data=df, x='Week Day', y='PowerConsumption_Zone3', label='Zone 3')

# Set title and labels
plt.title('Power Consumption According to Week Day')
plt.xlabel('Week Day')
plt.ylabel('Power Consumption')
plt.xticks(rotation=45)

# Add grid lines
plt.grid(True, linestyle='--', alpha=0.9)

# Tighten layout
plt.tight_layout()

# Show the plot
plt.show()


# Based on the graph, the data indicates that power consumption is at its lowest on Sundays in Zone 1 and Zone 2, while in Zone 3, the lowest consumption occurs on Fridays. Throughout the weekdays (Monday to Thursday), power usage remains relatively consistent in Zones 1 and 2, with Zone 1 consuming approximately 33,000 kWh and Zone 2 consuming around 22,000 kWh. In contrast, Zone 3 maintains a lower consumption level of approximately 18,000 kWh during the weekdays.

# In[83]:


# Increase the size of the heatmap
plt.figure(figsize=(10, 8))  # Adjust the width and height as needed

corr =df.corr()
# Create the heatmap
sns.heatmap(corr, cmap="YlGnBu", annot=True, fmt=".2f", linewidths=.5, cbar_kws={"shrink": .5})

# Set labels and title if needed

plt.title("Heatmap Showing the Correlation")

# Show the plot
plt.show()


# The heatmap above reveals strong positive correlations between Power Consumption in Zone 1 and Zone 2, standing at 0.83, and between Power Consumption in Zone 1 and Zone 3, registering at 0.75. However, the correlation between Zone 2 and Zone 3 is notably lower, at 0.57.
# 
# When considering the relationship between temperature and power consumption, the correlations are relatively weak across all zones. Notably, Zone 3 exhibits the highest correlation at 0.49. Conversely, there appears to be minimal positive correlation between windspeed and power consumption, with Zone 3 demonstrating the highest correlation coefficient at 0.28.
# 
# Furthermore, there exists a modest negative correlation between humidity and power consumption, ranging from -0.29 to -0.23 across the zones.

# In[ ]:




