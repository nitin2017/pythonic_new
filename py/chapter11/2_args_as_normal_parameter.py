# *args with normal parameter

def multiply_item(num,*args):
    print(num)
    print(args)
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

print(multiply_item(10,2,3)) # 6 here first arguement 10 is used by num and remaining (2,3) goes in args
print(multiply_item(10,2,3,4))
