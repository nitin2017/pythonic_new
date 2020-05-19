# generators are iterators 

# create your first generator with generator function

# 1. generator function 

# 10 ... 1 to 10

def nums(n):
    for i in range(1,n+1):
        yield(i) 

for number in nums(10):
    print(number)
print(nums(10)) # <generator object nums at 0x000001DB10718468>

# 2. generator comprehension 

square  = (i**2 for i in range(1,11))
print(square) # <generator object <genexpr> at 0x000001680D768468>
