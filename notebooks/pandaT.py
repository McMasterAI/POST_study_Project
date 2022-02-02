import pandas as pd
from sympy import content

#the data is a string (so dont convert input to int)
iD = input("Patient ID: ")
content = input("Column name: ")
id_col = pd.read_csv('./dta_file_converted.csv', low_memory=False)
data = id_col.loc[id_col['ices_caseid'] == iD]
print(data[content])


