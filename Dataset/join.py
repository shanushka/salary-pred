import pandas as pd


f1 = pd.read_csv('Banking.csv')
f2 = pd.read_csv('Banking1.csv')
f3 = pd.read_csv('Banking2.csv')

df_f = pd.concat([f1, f2, f3])
df_f["JobType"] = "Banking"
df_f["Industry"] = "Finance"

df_f.to_csv('finance.csv')

df_b = pd.read_csv('BusinessAnalyst.csv')
df_b["Industry"] = "Business"

df_b.to_csv('business.csv')

df_e = pd.read_csv('Environement_Specialists.csv')

df_e.to_csv('environment.csv')

# df_1 = pd.read_csv('StructuralEngineer.csv')
# df_2 = pd.read_csv('Transportationengineer.csv')


c1 = pd.read_csv('Civil_Engineering.csv')
c2 = pd.read_csv('ConstructionManagement.csv')
c3 = pd.read_csv('Geotechnicalengineering.csv')


# df_1["JobType"] =  "Structural Engineer"
# df_2["JobType"] = "Transportation Engineer"

c2["JobType"] = "Construction Management"
c3["JobType"] = "Geotechnical Engineer"

# df = pd.concat([df_2, df_1])

df_c = pd.concat([c1, c2, c3])

# df["Industry"] =  "Civil Engineering"

df_c["Industry"] = "Civil Engineering"

df_c.to_csv('CivilEngineering.csv')

el1 = pd.read_csv('RenewableEngineer.csv')
el2 = pd.read_csv('SystemEmbeddedEngineer.csv')

el1["JobType"] = "Renewable Engineer"
el2["JobType"] = "System Embedded Engineer"

df_el = pd.concat([el1, el2])
df_el["Industry"] = "Electrical Engineering"
df_el.to_csv('Electrical.csv')


h1 = pd.read_csv('HumanResource0.csv')
h2 = pd.read_csv('HumanResource1.csv')
h3 = pd.read_csv('HumanResource2.csv')
h4 = pd.read_csv('HumanResource3.csv')

df_h = pd.concat([h1, h2, h3, h4])
df_h["JobType"] = "Human Resource"
df_h["Industry"] = "Management"

df_h.to_csv('HumanResource.csv')


s1 = pd.read_csv('SoftwareDeveloper0.csv')
s2 = pd.read_csv('SoftwareDeveloper1.csv')
s3 = pd.read_csv('SoftwareDeveloper2.csv')
s4 = pd.read_csv('SoftwareDeveloper3.csv')
s5 = pd.read_csv('SoftwareDeveloper4.csv')
s6 = pd.read_csv('Backend.csv')

df_s = pd.concat([s1, s2, s3, s4, s5, s6])
df_s["JobType"] = "Developer"
df_s["Industry"] = "Software Development"

df_s.to_csv('SoftwareDeveloper.csv')


df = pd.concat([df_f, df_s, df_b, df_c, df_e, df_h, df_el])


df.to_csv("RawData.csv")
