from nltk.tokenize import sent_tokenize
from textblob import TextBlob
from train import find_feat, voteclass

l = []
score = 0

with open("new.txt") as file:
    for read in file:
        a = sent_tokenize(read)
        l.append(a)
        for i in a:
            analysis = TextBlob(i)
            #print(i, analysis.sentiment.polarity)
            score = score+analysis.sentiment.polarity
    #print(score)
    #print("\n")

    l = [j.replace("\n", "") for i in l for j in i]
    line = ""
    for i in l:
        line = line + " " + str(i)
    anal = TextBlob(line)
    feat = find_feat(line)
    print("classification : ", voteclass.classify(feat), "confidence :", voteclass.confidence(feat))
    score = 0
    line = ""
    l = []