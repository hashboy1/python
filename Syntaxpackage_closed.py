#testing program for decorate,packge closed and type convert
#decorate
def  comment(func):
    print(func)
    return func

#packageClosed
def packageClosed(number):
    def inner():
        print(str(number)+"inner function")
    return inner

@comment
def normalFunction():
    print("normalFunction")
    etc=packageClosed(0)
    etc()



normalFunction()
a=[1,2,3,4,5,1,2,3,4,5]
b={1:'a',2:'b',3:'c'}
print(a)
print(set(a))
print(tuple(a))