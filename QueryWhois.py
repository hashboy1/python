import socket
address = b"vr-kb.com \r\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('whois.internic.net', 43))
s.send(address)
response =b''
while True:
    data = s.recv(4096)
    response += data
    if not data :
        break
s.close()
print (response.decode())