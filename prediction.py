# import all required library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path="clean_data.csv"
df = pd.read_csv(path,header=None)
print("Done")

#to display the top 5 rows of the dataset
df.head(5)

from sklearn.linear_model import LinearRegression

#-------------------------analysis with simple linear regression---------------------------------------------#
lm = LinearRegression()
lm

lm.fit(df[['highway-mpg']],df[['price']])
lm

#printing the slope and intercept
lm.coef_
lm.intercept_

#printng the entire data to see what is the result
df

#-------------------------analysis with multiple linear regression------------------------------------------#

#using more than one independent variableslm.fit(Z, df['price'])
Z = df[['normalized-losses', 'highway-mpg']]
lm.fit(Z, df['price'])

#printing the slope and intercept
lm.coef_
lm.intercept_

#printing the entire data to see what is the result
df
