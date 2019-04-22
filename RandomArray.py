import numpy as np

res=input("please input the dimension of the array: ")
qty=int(res)
arr = np.arange(qty*qty)
np.random.shuffle(arr)
print(arr.reshape(qty,qty))