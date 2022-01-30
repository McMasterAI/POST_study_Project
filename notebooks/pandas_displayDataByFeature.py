import sys
import pandas as pd

# get data, replace quotation with path to data
df = pd.read_csv('../data/dta_file_converted.csv')

feature = sys.argv[1]

def display_data(feature):
    print(df[feature].iloc[0:100])

display_data(feature)