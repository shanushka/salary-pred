import pandas as pd


# df1 = pd.read_csv('Indeed_JD_Attorney.csv')
# df2 = pd.read_csv('Indeed_JD_LawClerk.csv')
# df3 = pd.read_csv('Indeed_JD_Paralegal.csv')
df1 = pd.read_csv('civilEngineering.csv')
df2 = pd.read_csv('Education.csv')
df3 = pd.read_csv('ElectricalEngineering.csv')
df4 = pd.read_csv('Finance.csv')
df5 = pd.read_csv('Health.csv')
df6 = pd.read_csv('HumanResources.csv')
df7 = pd.read_csv('InformationTechnology.csv')
df8 = pd.read_csv('MechanicalEngineer.csv')
df9 = pd.read_csv('RawData.csv')
df10 = pd.read_csv('renewableEngineering.csv')
df11 = pd.read_csv('ServiceIndustry.csv')
df12 = pd.read_csv('LegalService.csv')
df13 = pd.read_csv('SportsandRecreation.csv')
df14 = pd.read_csv('Tourism.csv')
df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14 ])
#df["Industry"] = "Human Resources"

# df_1  =pd.read_csv('RawData.csv')

# s = pd.concat([df, df_1])

df.to_csv("Data.csv")
