import sys
from hdfs.client import Client
client=Client("http://192.168.0.196:50070",root="/",timeout=100,session=False)

#proxy="gamer",
#with client.read( as fs:
#    content = fs.read()

#fs = client.content("/obj/obj/1.obj")
#print(fs)

#fs1=client.read("/obj/obj/1.obj").__enter__()
#print(type(fs1))
#content = fs1.read()
#print(content)



with client.read("/obj/obj/1.obj") as fs1:
      content = fs1.read()
      print(type(fs1))
      print(type(client.read("/obj/obj/1.obj")))
print(content)

#list all files
#print(client.list("/user/spark/output/"))
#client.makedirs("/dd")
#client.upload("/dd",r"d:\\student.txt")
#fs = client.content("/user/root/input/capacity-scheduler.xml")
