import pandas as pd


df1 = pd.read_csv('Indeed_JD_electricaldesignngineer.csv')
df2 = pd.read_csv('Indeed_JD_highvoltageengineer.csv')
df3 = pd.read_csv('Indeed_JD_powerelectronics.csv')
df4 = pd.read_csv('Indeed_JD_signalprocessing.csv')
df5 = pd.read_csv('Indeed_JD_systemembeddedengineer.csv')
df6 = pd.read_csv('Indeed_JD_transmissionlineengineer.csv')
df = pd.concat([df1, df2, df3, df4, df5, df6])


#df["JobType"] = "Banking"
#df["Industry"] = "Finance"

#df_1  =pd.read_csv('RawData.csv')

#s = pd.concat([df, df_1])

df.to_csv("Electricalengineer.csv")
