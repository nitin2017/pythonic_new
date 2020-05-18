# scope

x =5 # global variable
def func():
    x = 7 # scope of variable x is within function : func() this is local variable
    return x

def func2():
    print(x) # NameError: name 'x' is not defined

print(func())
print(x)

def func3():
    global x ### global keyword is used wen we want to override a global valriable inside a function
    x = 10
    print(x)

func3()
