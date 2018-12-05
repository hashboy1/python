from thrift.transport import TSocket,TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase

# thrift默认端口是9090
socket = TSocket.TSocket('192.168.0.196',9090)
socket.setTimeout(5000)

transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Hbase.Client(protocol)
socket.open()

print(client.getTableNames())
print(client.get('tPerformance','row1','cf:i'))
