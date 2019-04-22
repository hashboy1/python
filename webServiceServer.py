import sys
import socket
from spyne import Application, rpc, ServiceBase
from spyne import Integer, Unicode, Array, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class SomeSampleServices(ServiceBase):



    @rpc(Unicode, Unicode,_returns=Unicode)
    def make_project(self, name, version):
        #program detail


        print(name)
        print(version)
        return str(name)+str(version)


if __name__ == "__main__":
    soap_app = Application([SomeSampleServices],
                           'SampleServices',
                           in_protocol=Soap11(validator="lxml"),
                           out_protocol=Soap11())
    wsgi_app = WsgiApplication(soap_app)
    #ip="192.168.0.160"
    hostname = socket.gethostname()
    # 获取本机ip
    ip = socket.gethostbyname(hostname)
    print("ip address:" + ip)
    port=9090
    server = make_server(ip, port, wsgi_app)
#http://192.168.0.160:9090/SampleServices/lxml?wsdl

    sys.exit(server.serve_forever())
    print("Service Closed")