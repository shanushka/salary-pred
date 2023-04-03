import pandas as pd


df1 = pd.read_csv('Banking1.csv')
df2 = pd.read_csv('Banking2.csv')

df = pd.concat([df1, df2])


df["JobType"] = "Banking"
df["Industry"] = "Finance"

#df_1  =pd.read_csv('RawData.csv')

#s = pd.concat([df, df_1])

df.to_csv("2.csv")
