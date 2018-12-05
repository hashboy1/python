import urllib.request as rq

# content = rq.urlopen("http://www.ttmeiju.vip/latest.html").read()


# print(content)

# content.decode()
# rq.urlretrieve("http://www.ttmeiju.vip/", filename="d:/test/1.html")
mainurl = "http://www.ttmeiju.vip/latest.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = rq.Request(url=mainurl, headers=headers)
content = rq.urlopen(req).read()
fl = open("d:/test/1.html", "w")
fl.write(str(content))
fl.close()

# print(content)


# rq.urlretrieve(req, filename="d:/test/1.html")
