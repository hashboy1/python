import sys
import numpy as np
# from imp import *
# print(sys.path)
# reload(sys)
with open(r"d:\test.txt") as handleFile:
 data=handleFile.read();
 print("content1:"+data)
 data=handleFile.read();
 print("content2:"+data)
print(dir(np))
