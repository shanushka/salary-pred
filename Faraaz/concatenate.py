import pandas as pd


df1 = pd.read_csv('Indeed_JD_Attorney.csv')
df2 = pd.read_csv('Indeed_JD_LawClerk.csv')
df3 = pd.read_csv('Indeed_JD_Paralegal.csv')


df = pd.concat([df1, df2, df3 ])
#df["Industry"] = "Human Resources"

# df_1  =pd.read_csv('RawData.csv')

# s = pd.concat([df, df_1])

df.to_csv("Data science.csv")
