import jieba
import jieba.posseg as poss
import jieba.analyse as ana
# jieba.load_userdict() # load customize dictionary  盘古词库
sentence = "我爱天津的煎饼果子"
fl = open("TODO.txt", "r")
data = fl.read()



'''

w1 = jieba.tokenize(sentence)  #get position
for item in w1:
    print(item)
    
    
print(ana.extract_tags(data,3))   # get key word from string


w1 = poss.cut(sentence)
for item in w1:
    print(item.word+item.flag)

w1 = jieba.cut_for_search(data)
for item in w1:
    print(item)

w1 = jieba.cut(sentence, cut_all=True)
for item in w1:
    print(item)

w1 = jieba.cut(sentence, cut_all=False)
for item in w1:
    print(item)
'''