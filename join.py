import pandas as pd
df_1 = pd.read_csv('Indeed_JD_structuralengineer.csv')
df_2 = pd.read_csv('Indeed_JD_transportationengineer.csv')

df_1["JobType"] =  "Structural Engineer"
df_2["JobType"] = "Transportation Engineer"
df = pd.concat([df_2, df_1])

df["Industry"] =  "Civil Engineering"

df.to_csv("Civil_Engineering.csv")

