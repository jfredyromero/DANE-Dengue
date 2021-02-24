import pandas as pd
import numpy as np
from functions import normalize

dengue_data_file = "DANE_Dengue_Data_Variables.csv"
municipality_dataframe = pd.read_csv(dengue_data_file)

elevation_file = "Data_Files/Municipality_Elevation.csv"
elevation_dataframe = pd.read_csv(elevation_file, usecols=['altitude_MEAN'])

# Combino los dataframes por indice
municipality_dataframe = municipality_dataframe.join(elevation_dataframe)
# Cambio el nombre de la columna
municipality_dataframe.rename(columns={'altitude_MEAN':'Altitude Mean (m)'}, inplace=True)
municipality_dataframe['Altitude Mean (m)'] = municipality_dataframe['Altitude Mean (m)'].str.replace(",", ".").astype(float)
municipality_dataframe['Altitude Mean (m)'] = pd.to_numeric(municipality_dataframe['Altitude Mean (m)'], errors='coerce')
# Creating the csv file
municipality_dataframe.to_csv('DANE_Dengue_Data_Variables.csv', index=False)
