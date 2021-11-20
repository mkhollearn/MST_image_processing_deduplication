import pandas as pd

#counts the number of rows in the dataset based on the lure rating

df = pd.read_csv('final_output.csv')
df = df[['Lure Rating']]
print(df[['index','Lure Rating']].groupby('Lure Rating').count())

#output: Lure Rating       
#1.0            203
#2.0            194
#3.0            201
#4.0            214
#5.0            211
#these are image pairs because the lure rating was only assingned to one of the two images during data processing