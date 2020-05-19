# define a decorator @ calculate time 
# def func():
#     print(this is a function)

# func():
# this function took 3 secs to run 

import time 
from functools import wraps


def calculate_time(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        print(f"Executing  ...... {function.__name__}")
        t0 = time.time()
        returned_value = function(*args,**kwargs)
        t1 = time.time()
        diff = t1 -t0
        print(f"This function took {diff} seconds ")
        return returned_value 
    return wrapper_function

@calculate_time
def square_finder(n):
    return [i**2 for i in range(1,n+1)]


square_finder(1000 )

