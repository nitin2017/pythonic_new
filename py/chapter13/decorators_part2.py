from functools import wraps
def decorator_function(any_func):
    @wraps(any_func)
    def wrapper_function(*args,**kwargs):
        """ THIS IS WRAPPER FUNCTION """
        print('This is awesome function')
        return any_func(*args,**kwargs)
    return wrapper_function

# @decorator_function
# def func():
#     print("This is function")

# func()

# @decorator_function
# def func1(a):
#     print(f"This is function with arguement {a}") 

# func1(7)

@decorator_function
def add(a,b):
    """THIS IS ADD FUNCTION """
    return a+b 

print(add(2,3))

print(add.__doc__)
print(add.__name__)
