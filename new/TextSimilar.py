import gensim
import jieba
from collections import defaultdict
from tqdm import tqdm

doc1 = "t1.txt"
doc2 = "t2.txt"

d1 = open(doc1, "r").read()
d2 = open(doc2, "r").read()

data1 = jieba.cut(d1)
data2 = jieba.cut(d2)

'''
data11 = ""
data21 = ""

for item in data1:
    data11 = data11 + item + " "

for item in data2:
    data21 = data21 + item + " "


documents = [data11, data21]

texts = [[word for word in document.split()] for document in documents]


print(texts)
'''

text1 = []
text2 = []
for item in data1:
    text1.append(item)
for item in data2:
    text2.append(item)
texts = [text1, text2]

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1
#print(frequency)
dictionary = gensim.corpora.Dictionary(texts)
dictionary.save("dictionary.txt")

d3 = open("t3.txt").read()
data3 = jieba.cut(d3)
corpus = [dictionary.doc2bow(data3)]
tfidf = gensim.models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
print(tfidf)