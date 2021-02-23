import pandas as pd
import numpy as np
from functions import normalize

dengue_data_file = "DANE_Dengue_Data_Variables.csv"
municipality_dataframe = pd.read_csv(dengue_data_file)

elevation_file = "Data_Files/Municipality_Elevation.csv"
elevation_dataframe = pd.read_csv(elevation_file, usecols=['altitude_MEAN'])

# Combino los dataframes por indice
municipality_dataframe = municipality_dataframe.join(elevation_dataframe)
# Creating the csv file
municipality_dataframe.to_csv('DANE_Dengue_Data_Variables.csv', index=False)
