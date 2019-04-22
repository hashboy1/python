import pymysql

conn=pymysql.connect(host='192.168.0.160',user='3dms',password='vrkb',database='3dmsv2',charset='utf8mb4')
cur=conn.cursor()
cur.execute("select * from model_master")
row=cur.fetchall()

#print(type(row))
#print((row))
#print(row)
#print(type(row[0]))
#print(row[0])



#for i in range(160,len(row)):
#    print(row[i])
#print(len(row))

for content in list(row):
     print(content)


conn.close()