import pandas as pd


df1 = pd.read_csv("Indeed_JD_PersonalTrainer.csv")
df2 = pd.read_csv("Indeed_JD_Referee.csv")
df3 = pd.read_csv("Indeed_JD_SportsCoach.csv")
#df4 = pd.read_csv("Indeed_JD_HotelManager.csv")
#df5 = pd.read_csv("Indeed_JD_TravelAgent.csv")
#df6 = pd.read_csv("Indeed_JD_Photographer.csv")
#df7 = pd.read_csv("Indeed_JD_TatooArtist.csv")

df1["JobType"] = "PersonalTrainer"
df2["JobType"] = "Referee"
df3["JobType"] = "SportsCoach"
#df4["JobType"] = "Hotel Manager"
#df5["JobType"] = "Travel Agent"
#df6["JobType"] = "Photographer"
#df7["JobType"] = "Tatoo Artist"

df = pd.concat([df1, df2, df3 ])


df["Industry"] = "Sport and Recreation"

#df_1  =pd.read_csv('RawData.csv')

#s = pd.concat([df, df_1])

df.to_csv("SportsandRecreation.csv")
