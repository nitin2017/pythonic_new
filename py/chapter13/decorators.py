# decorators - enhance the functionality of other functions 
# @ use for decorators 



def func2():
    print("this is function 2")

def decorator_function(any_func):
    def wrapper_function():
        print('This is awesome function')
        any_func()
    return wrapper_function

@decorator_function
def func1():
    print("this is function 1")

# var1  = decorator_function(func1)
# var1()

# var2  = decorator_function(func2)
# var2()

# func1  = decorator_function(func1)
# func1()

func1()