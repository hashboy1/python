import socket

sk = socket.socket()
sk.connect(("192.168.0.160", 8099))  # 主动初始化与服务器端的连接
while True:
    send_data = input("输入发送内容:")
    send_data= send_data +" \n"
    #print(send_data)
    sk.sendall(bytes(send_data, encoding="utf8"))
    if send_data == "byebye":
        break
    accept_data = str(sk.recv(1024), encoding="utf8")
    print("接收内容：", accept_data)
sk.close()