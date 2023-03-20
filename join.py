import pandas as pd
df = pd.read_csv('environementspecialist.csv')
df_1 = pd.read_csv('environementspecialist_1.csv')
df_2 = pd.read_csv('environementspecialist_2.csv')
df_3 = pd.read_csv('environementspecialist_3.csv')
df_4 = pd.read_csv('environementspecialist_4.csv')
df_5 = pd.read_csv('environementspecialist_5.csv')
df_6 = pd.read_csv('environementspecialist_6.csv')
df_7 = pd.read_csv('environementspecialist_7.csv')
df_8 = pd.read_csv('environementspecialist_8.csv')
df_9 = pd.read_csv('environementspecialist_9.csv')

df = pd.concat([df, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9])
df["JobType"] =  "Environment Specialist"

df.to_csv("Environement_Specialist.csv")

