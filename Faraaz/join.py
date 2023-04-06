import pandas as pd


df1 = pd.read_csv("Indeed_JD_constructionmanagement.csv")
df2 = pd.read_csv("Indeed_JD_transportationengineer.csv")
df3 = pd.read_csv("Indeed_JD_waterresourcesengineer.csv")
df4 = pd.read_csv("Indeed_JD_structuralengineer.csv")
df5 = pd.read_csv("Indeed_JD_Geotechnicalengineering.csv")
df6 = pd.read_csv("Indeed_JD_surveyor.csv")

df1["JobType"] = "Construction Management"
df2["JobType"] = "Transportation Engineering"
df3["JobType"] = "Water Resource Engineering"
df4["JobType"] = "Structural Engineering"
df5["JobType"] = "Geotechnical Engineering"
df6["JobType"] = "Surveyor"




df = pd.concat([df1, df2, df3, df4, df5, df6])


df["Industry"] = "Civil Engineer"

#df_1  =pd.read_csv('RawData.csv')

#s = pd.concat([df, df_1])

df.to_csv("civilengineer.csv")
