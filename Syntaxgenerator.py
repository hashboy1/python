import scrapy
import re
def geneNum():
     num=0
     while num<100:
          if num%2!=0 and num%3!=0:
            yield num
            num = num + 1
          else:
            num = num + 1


func= geneNum()
#print(func.__next__())

for i in func:
    print(i)


