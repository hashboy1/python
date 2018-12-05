import sqlalchemy as sa
kylin_engine = sa.create_engine('kylin://ADMIN:KYLIN@192.168.0.196:7070/fisrtproject?version=v1')
results = kylin_engine.execute('SELECT MODEL_NAME FROM MODEL_MASTER')
print(results)
print(kylin_engine.table_names())