from suds.client import Client

#test=Client('http://192.168.0.160:8080/Service/ServiceHello?wsdl')
#print(test.service.getValue('hello'))

test=Client('http://192.168.0.160:9090/SampleServices/lxml?wsdl')
print(test.service.make_project('new','1.0.0'))
