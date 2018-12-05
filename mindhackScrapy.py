import urllib as ul


data=ul.request.urlopen("http://mindhacks.cn/")
print(data.read())



