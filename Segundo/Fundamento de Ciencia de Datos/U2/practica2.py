import pandas as pd
import os

## Ejercicio 1 #########################################################################

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "datasets", "flete-aereo-vacunas-covid19-al-2021-06-28.xlsx")
dataset = pd.read_excel(file_path)
dataset.info()
