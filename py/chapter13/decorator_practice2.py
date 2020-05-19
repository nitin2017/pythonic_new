# only int allow 

from functools import wraps

def only_int_allow(any_func):
    @wraps(any_func)
    def wrapper_function(*args,**kwargs):
        if all([(type(arg)==int) for arg in args]):
            return any_func(*args,**kwargs)
        else:
            print("Invalid arguements")
    return wrapper_function

@only_int_allow
def add_all(*args):
    total = 0 
    for i in args :
        total+=i
    return total

print(add_all(1,2,3,4,5,[6,7,8]))
print(add_all(1,2,3,4,5))