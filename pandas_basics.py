
#Pandas basics – Series, DataFrame, data loading, data selection, filtering, aggregation, handling missing data, merging, and grouping.
import pandas as pd

#series creation
s=pd.Series([10,20,30,40],index=['a','b','c','d'])
print(s)
#dataframe creation
data={'Name':['Alice','Bob','Charlie','David'], 'Age':[24,27,22,32], 'City':['NY','LA','SF','CHI']}
df=pd.DataFrame(data)
print(df)
#data loading

df=pd.read_csv('heart.csv')
print(df.head())
#data selection
print(df['sex'])   
print(df.loc[0])
print(df.iloc[1:3])
#filtering
print(df[df['age']>25]) 
#aggregations
print(df['age'].mean())


#handling missing data
df.fillna(0, inplace=True)
print(df)
#merging
df1=pd.DataFrame({'ID':[1,2,3],'Score':[85,90,95]})
df2=pd.DataFrame({'ID':[1,2,3],'Grade':['A','A','A']})
merged_df=pd.merge(df1, df2, on='ID')
print(merged_df)
#grouping
grouped=df.groupby('ca')['age'].mean()
print(grouped)



