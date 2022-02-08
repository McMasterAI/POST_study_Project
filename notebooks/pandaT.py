import pandas as pd
from sympy import content
import numpy as np

#the data is a string (so dont convert input to int)
iD = input("Patient ID: ")
id_col = pd.read_csv('./dta_file_converted.csv', low_memory=False)
data = id_col.loc[id_col['ices_caseid'] == iD]
arr = np.array(
    [

    [
        data['ices_opioidbase'].tolist()[0], 
        data['ices_opioid3'].tolist()[0],
        data['ices_opioid6'].tolist()[0],
        data['ices_opioid9'].tolist()[0],
        data['ices_opioid12'].tolist()[0],

    ],

    [
        data['ices_amountdose'].tolist()[0],
        data['ices_currdose3'].tolist()[0],
        data['ices_currdose6'].tolist()[0],
        data['ices_currdose9'].tolist()[0],
        data['ices_currdose12'].tolist()[0],
    ]

    ]   
    )

print(arr)



