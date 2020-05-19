# function returning function

def square(a):
    return a**2 


def outer_func(msg):
    def inner_func():
        print(f"message is {msg}")
    return inner_func

print(outer_func()) # <function outer_func.<locals>.inner_func at 0x000001E4528A02F0>
var = outer_func()
var()