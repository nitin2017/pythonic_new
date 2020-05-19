# pass function as an arguement

l = [1,2,3,4]
def square(a):
    return a**2
print(list(map(square,l))) 


def my_map(func,l):
    return [func(i) for i in l]

print(my_map(square,l))