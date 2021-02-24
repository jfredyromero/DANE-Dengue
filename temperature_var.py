#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


dengue_data_file = "DANE_Dengue_Data_Variables.csv"
municipality_dataframe = pd.read_csv(dengue_data_file)


# In[7]:


Temperature_file = "Data_Files/Municipality_Temperature.csv"
Temperature_dataframe = pd.read_csv(Temperature_file, usecols=['Temperature'])


# In[6]:



# Combino los dataframes por indice
municipality_dataframe = municipality_dataframe.join(Temperature_dataframe)


# In[12]:


# Creating the csv file
municipality_dataframe.to_csv('DANE_Dengue_Data_Variables.csv', index=False)
print(municipality_dataframe)


# In[ ]:




