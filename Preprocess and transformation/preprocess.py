import pandas as pd

businessAnalystSkill = {"agile", "sql queries", 
"project management", "analytical and critical thinking", "big data analysis", "project planning tool", 
"database", "communication","Visualizations" ,"Power Bi"}

df = pd.read_csv('BusinessAnalyst.csv')

def find_words_in_sentence(words, sentence):
    word_list = []
    for word in words:
        if word in sentence:
            word_list.append(word)
    return word_list

wordlists = []

for des in df['Job Description']:
  wordlist = find_words_in_sentence(businessAnalystSkill, des) 
  wordlists.append(wordlist)

df['Skill'] = wordlists

df.to_csv("BusinessAnalyst_Skill.csv")
