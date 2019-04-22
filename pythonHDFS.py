import sys
from hdfs.client import Client
client=Client("http://192.168.0.196:50070",root="/",proxy="gamer",timeout=100,session=False)
#with client.read( as fs:
#    content = fs.read()

#fs = client.read("/user/root/input/capacity-scheduler.xml")
#list all files
#print(client.list("/user/spark/output/"))
client.makedirs("/dd")
client.upload("/dd",r"d:\\student.txt")
#fs = client.content("/user/root/input/capacity-scheduler.xml")
