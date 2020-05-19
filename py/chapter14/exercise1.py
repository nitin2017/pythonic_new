# define a generator function 
# take one number as arguement 
# generate a sequence of even numbers from 1 to that number 


def is_even(n):
    for num in range(1,n+1):
        if num%2==0:
            yield(num)

for num in is_even(20):
    print(num)