# lambda expressions (anaonymous functions ) 

def add(a,b):
    return a+b

add2 = lambda a,b:a+b 
print(add2(2,3))

# we generally use lambda expression with built in function 

multiply = lambda a,b:a*b 
print(multiply(2,3))

print(add) # <function add at 0x000001CBE4482F28>
print(add2) # <function <lambda> at 0x000001CBE4910268>
print(multiply)

def is_even(a):
    return a%2 == 0

result =  lambda a:a%2 ==0
print(result(3)) # False
print(result(4)) # True 
