# only int allow 

from functools import wraps

def only_data_type_allow(data_type):
    def decorator(any_func):
        @wraps(any_func)
        def wrapper_function(*args,**kwargs):
            if all([(type(arg)==data_type) for arg in args]):
                return any_func(*args,**kwargs)
            else:
                print("Invalid arguements")
        return wrapper_function
    return decorator


@only_data_type_allow(str)
def string_join(*args):
    string=''
    for i in args:
        string += i
    return string

print(string_join('nitin', ' choudhary',8))
print(string_join('nitin', ' choudhary'))