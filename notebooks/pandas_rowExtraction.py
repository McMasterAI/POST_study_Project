import pandas as pd
import sys
import argparse

df = pd.read_csv('C:/Users/aidan/Downloads/dta_file_converted.csv', low_memory=False)

# pd.set_option("display.max_rows", None, "display.max_columns", None)

parser = argparse.ArgumentParser()
parser.add_argument("--rownum")
parser.add_argument("--patientID")
args = parser.parse_args()


def rowData():
    if not (args.rownum):
        print("Please input the row number!")
        sys.exit()
    
    rowNum = args.rownum
    
    print(df.loc[int(rowNum),:])


def patientID():
    if not (args.patientID):
        print("Please input the patient ID!")
        sys.exit()
    
    ID = args.patientID

    print(df.loc[df['ices_caseid'] == ID])


rowData()
patientID()
