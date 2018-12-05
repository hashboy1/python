import struct
import os

#a = struct.pack('<IIII',3,4,5,6)
#a = b'hello'
#b = b'world!'
#c = 2
#d = 45.123
#bytes = struct.pack('5s6sif', a, b, c, d)
#print(bytes)
# filepath=r"E:\workspace\python\ship.bin"
# binfile=open(filepath,'rb')
# print(binfile.read())

a='0'
bytes = struct.pack('i', int('4'))


databinary = [ ]

filehandler=open("data/40coupe.obj","r")
data = filehandler.readline()
while (data):
    # print(data)
    if data.find("#") >=0 or data == "":
        a=1
    else:
        for i in range(len(data)):
            if data[i].isdigit():
               bytes = struct.pack("<iiii",int(data[i]),0,0,0)


            else:
               bytes = struct.pack("<ssss", data[i].encode(),b'0',b'0',b'0')
            #print(bytes)
            databinary.append(bytes)

    data = filehandler.readline()

filehandler.close()

# bytesText = databinary.encode()


filehandler2 = open("data/40coupe.bin", "wb")
filehandler2.write(b"".join(databinary))
filehandler2.close()
