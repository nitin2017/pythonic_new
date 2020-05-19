# @ print function data 

from functools import wraps

def print_function_data(any_func):
    @wraps(any_func)
    def wrapper_func(*args,**kwargs):
        print(f"you are calling {any_func.__name__} function")
        print(f"{any_func.__doc__}")
        return any_func(*args,**kwargs)
    return wrapper_func

@print_function_data
def add(a,b):
    """This function takes two arguements and return their sum"""
    return a+b 

print(add(2,5))

