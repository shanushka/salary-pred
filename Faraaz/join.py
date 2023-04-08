import pandas as pd


df = pd.read_csv("Indeed_JD_renewableengineer.csv")
#df2 = pd.read_csv("Indeed_JD_highvoltageengineer.csv")



df["JobType"] = "renewableengineer"
#df2["JobType"] = "highvoltageengineer"




#df = pd.concat([df1, df2, df3, df4, df5, df6])


df["Industry"] = "renewable engineering"

#df_1  =pd.read_csv('RawData.csv')

#s = pd.concat([df, df_1])

df.to_csv("renewable engineering.csv")
