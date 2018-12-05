from pyhive import hive

conn = hive.Connection(host='192.168.0.196', port=10000,  database='default')#host主机ip,port：端口号，username:用户名，database:使用的数据库名称
cursor=conn.cursor()
cursor.execute('select * from tPerformance limit 10')#执行查询
for result in cursor.fetchall():
     print(result)                      #将查询结果打印出来
