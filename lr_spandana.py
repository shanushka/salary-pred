# -*- coding: utf-8 -*-
"""Copy of lr and cnn

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lqFXCTnHR5KnRNGH1qsgMYAvqRDLyx18
"""

import pandas as pd
import numpy as np
import seaborn as sns

d1 = pd.read_csv("/content/flabel12.csv")
d2 = pd.read_csv("/content/dataairport1.csv")
d3 = pd.read_csv("/content/datachruch1.csv")
d4 = pd.read_csv("/content/datahospital1.csv")
d5 = pd.read_csv("/content/datarestaurant.csv")
d6 = pd.read_csv("/content/datazoo1.csv")

data = pd.concat([d1,d3,d4,d5,d6])
data.shape

data.drop_duplicates(subset=['Tweet'], inplace = True)
print("No of Unique tweets: ", data['Tweet'].count())

import nltk
import re, string
from nltk.corpus import stopwords
nltk.download('stopwords')
stopword = stopwords.words('english')
print("Stopwords:",stopword)

def clean(text):
    text = text.lower() # lower case
    text = re.sub(r'https?://\S+|www\.\S+', " ", text)#URL
    text = re.sub(r'@\w+',' ',text) # mentions
    text = re.sub(r'#\w+', ' ', text) #hashtags
    text= re.sub(r'[^\w\s]',' ',text) #punctuations
    text= re.sub(r'\d+', ' ', text) #digits
    text = re.sub('\[.*?\]',' ', text) #any punctuations left
    text = re.sub("[^a-z0-9]"," ", text)# any others charcters other than numbers and letters
    text = text.split() #stopwords
    text = " ".join([word for word in text if not word in stopword])
    return text

data['Tweet'] = data['Tweet'].astype(str).apply(lambda x: clean(x))
data['Tweet'].sample(5)

max_len = len(max(data['Tweet'], key=len))
print("Maximum length of Tweet:",max_len)

import nltk
nltk.download('omw-1.4')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = WordNetLemmatizer()
def lemmatize_tweets(tweets):
    temp = ""
    for w in tokenizer.tokenize(tweets):
      temp = temp + lemmatizer.lemmatize(w) +" " 
    return temp
data['Tweet'] = data['Tweet'].apply(lambda x: lemmatize_tweets(x))

from nltk.stem.porter import PorterStemmer
stemmer= PorterStemmer()

def stem_tweets(tweets):
    temp = ""
    for w in tokenizer.tokenize(tweets):
      temp = temp + stemmer.stem(w) +" " 
    return temp
data['Tweet'] = data['Tweet'].apply(lambda x: stem_tweets(x))

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

x = data['Tweet']
y = data['Label']

train_X, test_X, train_Y, test_Y = train_test_split(x, y, test_size = 0.2, random_state=42)

train_X.shape

encoder = LabelEncoder()
train_Y = encoder.fit_transform(train_Y)
test_Y = encoder.fit_transform(test_Y)

vectorizer = CountVectorizer(ngram_range= (1,3)).fit(train_X)
train_X_cv = vectorizer.transform(train_X)
test_X_cv = vectorizer.transform(test_X)

lr = LogisticRegression(penalty="l2",multi_class = "multinomial",solver = "saga", C=1, max_iter=5000)
lr.fit(train_X_cv,train_Y)
lr_pred = lr.predict(test_X_cv)
print("LR CV Accuracy Score -> ",accuracy_score(lr_pred,test_Y)*100)

lr_cm = confusion_matrix(test_Y, lr_pred, normalize="true")
sns.heatmap(lr_cm ,annot=True)
from sklearn.metrics import f1_score
print(f1_score(test_Y, lr_pred, average='macro'))
print(classification_report(test_Y,lr_pred))

vectorizer = TfidfVectorizer(ngram_range= (1,3)).fit(train_X)
train_X_tfidf = vectorizer.transform(train_X)
test_X_tfidf = vectorizer.transform(test_X)

lr1 = LogisticRegression(penalty="l2",multi_class = "multinomial",solver = "saga", C=1, max_iter=5000)
lr1.fit(train_X_tfidf,train_Y)
lr1_pred = lr.predict(test_X_tfidf)
print("LR TFIDF Accuracy Score -> ",accuracy_score(lr1_pred, test_Y)*100)

from sklearn.metrics import confusion_matrix
lr1_cm = confusion_matrix(test_Y, lr1_pred, normalize="true")
sns.heatmap(lr1_cm ,annot=True)
from sklearn.metrics import f1_score
print(f1_score(test_Y, lr1_pred, average='macro'))
print(classification_report(test_Y,lr1_pred))