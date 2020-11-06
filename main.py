from nltk.tokenize import sent_tokenize
import pickle
from textblob import TextBlob

l1 = []
business = {}

for i in range(1, 386):
    if i < 10:
        k = "0"+"0"+str(i)
    elif i < 100:
        k = "0"+str(i)
    else:
        k = str(i)
    l1.append(k)

l = []
count = 0
count1 = 0
count2 = 0
score = 0

for i in l1:
    with open("bbc/politics/"+str(i)+".txt") as file:
        for read in file:
            a = sent_tokenize(read)
            l.append(a)
            for i in a:
                analysis = TextBlob(i)
                #print(i, analysis.sentiment.polarity)
                score = score+analysis.sentiment.polarity
        l = [j.replace("\n", "") for i in l for j in i]
        line = ""
        for i in l:
            line = line+" "+str(i)
        if score > 0:
            count = count+1
            business[line] = 1
        elif score < 0:
            count1 = count1+1
            business[line] = -1
        else:
            count2 = count2+1
            business[line] = 0
        score = 0
        line = ""
        l = []

print(count, count1, count2)
with open("politic.pickle", 'wb') as dic:
    pickle.dump(business, dic, protocol=pickle.HIGHEST_PROTOCOL)
