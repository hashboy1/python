'''
k=2
n=302
count = 0
for i in range(k, n+1):
    print(i)
    print(str(i).count("1"))
    count=count+str(i).count("1")
    #if str(i).find("1") != -1:
    #    count = count + 1
    #else:
     #   count = count
print(count)
'''

a = "333311"
print(a.isnumeric())