import jieba
import jieba.posseg as po
import jieba.analyse as ana
import urllib




fh=  open("D:\logs\live-ecommence.log","r")
content = fh.read()


w1= po.cut(content)

for i in w1:
    print(i.word+"----"+i.flag)

w = ana.extract_tags(content,10)
print(w)


uh = urllib.request.urlopen("https://www.cnblogs.com/leomei91/p/7352646.html")

w2= ana.extract_tags(uh.read())
print(w2)