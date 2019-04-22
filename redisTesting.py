import redis
# r = redis.Redis(host='192.168.0.160', port=6379,db=0)
# pool = redis.ConnectionPool(host='192.168.0.160', port=6379)

pool = redis.ConnectionPool(host='192.168.0.196', port=7001)
r = redis.Redis(connection_pool=pool)

pipe = r.pipeline(transaction=True)

#r.set('name', 'zhangsan')
# r.set('name', 'lisi')

b = r.get('name')
print(b)
#pipe.execute()

