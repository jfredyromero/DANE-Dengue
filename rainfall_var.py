import pandas as pd
import numpy as np
from functions import normalize

dengue_data_file = "DANE_Dengue_Data_Variables.csv"
municipality_dataframe = pd.read_csv(dengue_data_file)
final_file = municipality_dataframe.copy()
municipality_dataframe = municipality_dataframe[['State','Municipality code']]

rainfall_file = "Data_Files/Municipality_Rainfall.csv"
rainfall_dataframe = pd.read_csv(rainfall_file)

rainfall_dataframe['Area (km²)'] = rainfall_dataframe['Area (km²)'].str.replace(",", ".").astype(float)
rainfall_dataframe['Area (km²)'] = pd.to_numeric(rainfall_dataframe['Area (km²)'], errors='coerce')
rainfall_dataframe['Rainfall per km2'] = rainfall_dataframe['Rainfall']/rainfall_dataframe['Area (km²)']
del rainfall_dataframe['Rainfall']
del rainfall_dataframe['Area (km²)']
del rainfall_dataframe['Department Name']

for i in range(len(rainfall_dataframe['Municipality Name'])-1):
    if rainfall_dataframe.loc[i,'Municipality Name'] ==  rainfall_dataframe.loc[i+1,'Municipality Name']:
        rainfall_dataframe.loc[i+1,'Rainfall per km2'] += rainfall_dataframe.loc[i,'Rainfall per km2']
        rainfall_dataframe.drop(i, inplace=True)
rainfall_dataframe = rainfall_dataframe.reset_index(drop=True)
del rainfall_dataframe['Municipality Name']

municipality_dataframe.sort_values(['State','Municipality code'], inplace=True)
municipality_dataframe = municipality_dataframe.reset_index(drop=True)
del municipality_dataframe['State']
municipality_dataframe = municipality_dataframe.join(rainfall_dataframe)

# Combino los dataframes por indice
final_file = pd.merge(final_file, municipality_dataframe, on='Municipality code', how='outer')
# Creating the csv file
final_file.to_csv('DANE_Dengue_Data_Variables.csv', index=False)
