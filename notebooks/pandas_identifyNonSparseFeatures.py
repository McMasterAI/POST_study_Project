from numpy import append
import pandas as pd

# get data, replace quotation with path to data
df = pd.read_csv('../data/dta_file_converted.csv')

# the top 'num_features' most full features will be identified
num_features = 100

num_nulls = df.isnull().sum()
num_nulls.sort_values(inplace=True)


# the following section considers all features
fewest_null_features = []
for i in range(num_features):
    fewest_null_features.append((num_nulls.index[i], num_nulls[i]))

# tuple: (feature name, num of nulls within feature)
print(fewest_null_features)
print('\n')


# the following section considers features with more than one unique value
# gto = greater than one
gto_unique_value_features = []
for i in range(num_features):
    if df[num_nulls.index[i]].nunique() > 1:
        gto_unique_value_features.append((num_nulls.index[i], num_nulls[i], df[num_nulls.index[i]].nunique()))

# tuple: (feature name, num of nulls within feature, number of unique values)
print(gto_unique_value_features)