# function returning two values

def func(int1,int2):
    add = int1 + int2 
    multiply = int1 * int2 
    return add,multiply

print(func(2,3)) # (5, 6) this will return tuple

add , multiply = func(2,3) # unpacking tuple
print(add)  # 5
print(multiply) # 6