# define a function
# input 
# num , iterable(tuple,list) containing number as args
# example 
# nums = [1,2,3]
# to_power(3,*nums)

# output
# list -----> [1**3,8,27]

# if user didn't pass any args then give a user message 'hey you didn't passed anything'

# else return list

# use list comprehension 



def to_power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        return "Hey you didn't passed any args"

l1 = [1,2,3,4]
l2 =[]

print(to_power(2,*l1)) # [1, 4, 9, 16]
print(to_power(2,*l2)) # Hey you didn't passed any args