import struct
import os

fileHandle = open(r"data/40coupe.bin",'rb')
byte1 = fileHandle.read()
#print(byte1.decode('utf-8'))
print(len(byte1))
#print(byte1)
for i in range(100):
     print(byte1[i])

'''
for i in range(len(byte)):
       if  str(byte[i]).isdigit():
              data = struct.unpack("<i",byte[i])
       else:
              data = struct.unpack("<s",byte[i])

'''