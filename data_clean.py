#data pre processing performed before analysis
import pandas as pd
import numpy as np

path="automobile.csv"

#read the file
df = pd.read_csv(path,header=None)
print("Done")

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)
df.head(5)

missing_data = df.isnull()
missing_data.head(5)

#count the missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("") 

#replace the missing 'num-of-doors' values by the most frequent because four is the most frequently occured value in the data
df["num-of-doors"].replace(np.nan, "four", inplace = True)

# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace = True)

# reset index, because we droped two rows
df.reset_index(drop = True, inplace = True)

#data standardization and normalization
# transform mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]

# check your transformed data 
df.head()

# replace (origianl value) by (original value)/(maximum value)
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()

#save the cleaned dataset
df.to_csv('clean_df.csv')

