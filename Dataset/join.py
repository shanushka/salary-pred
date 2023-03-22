import pandas as pd


df = pd.read_csv('Teacher.csv')


df["JobType"] = "Teaching"
df["Industry"] = "Education"

df_1  =pd.read_csv('RawData.csv')

s = pd.concat([df, df_1])

s.to_csv("RawDataset.csv")
