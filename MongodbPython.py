import os
from pymongo import MongoClient
import gridfs
from bson.objectid import ObjectId
import bson
from bson.codec_options import CodecOptions
import pymysql

#connect to mysql
#MySqlConn=pymysql.connect(host='192.168.0.249',user='vrkb',password='3dms',database='3dmsv2',charset='utf8mb4')
#cur=MySqlConn.cursor()

#connect to MongoDB
MongoDBconn = MongoClient("mongodb://vrkb:vrkb0702@192.168.0.249:30000/")
db = MongoDBconn["model_vrkb"]
tempFolder="f:\\temp\\"


#list files basic information

list1=db['model201807.files']
fs = gridfs.GridFS(db, 'model201807')
for i in list1.find():
    id = i['_id']
    filename=i['filename']
    metadata=i['metadata']
    modelId=metadata['modelId']
    record = fs.get(ObjectId(id));
    print("filename:"+record.filename)
    data = record.read()
    if not os.path.exists(tempFolder+modelId):
        os.makedirs(tempFolder+modelId)
    out = open(tempFolder+modelId+"\\"+filename,'wb')
    out.write(data)
    out.close()
    # print(i)
    #print(filename)
    #print(modelId)
    #cur.execute("select * from model_master")



'''
list1=db['model201807.chunks']
for i in list1.find():
    print(i['_id'])
    print(i['files_id'])
    #print(i['data'].decode('gbk'))
    #print(bson.BSON.decode(i['data']))
    #print(bson.binary.Binary(i['data']))
    print(bson.is_valid(i))
'''

#read the file from the mongodb gridFS
'''
fs = gridfs.GridFS(db, 'model201807')
list2 = fs.list()   #just the list of filename
record=fs.get(ObjectId("5b51a0493013932b11bf4f8a"))
data=record.readchunk()
#print(data)
out = open('d:\\a.png','wb')
out.write(data)
out.close()
'''

'''
for i in list2:
    fs.get(i)
    print(type(i))
'''
#MySqlConn.commit()
#MySqlConn.close()
MongoDBconn.close()




'''

list1=db.collection_names('model201807.files')
for i in list1:
    print(i)

my_set = db["Collections"]
for i in my_set.find():
    print(i)
'''