# # make flexible function

# * operator 
# *args 

def total(a,b):
    return a+b 

print(total(2,3)) # 5
# print(total(2,3,9,10)) # TypeError: total() takes 2 positional arguments but 4 were given

# In order to solve above problem we use * operator

def all_total(*args): # * will start taking tuple as arguement and we can pass as many numbers now args is convention we use any word here
    print(args) # (1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(type(args)) # <class 'tuple'>
    sum = 0
    for num in args:
        sum += num
    return sum

print(all_total(1,2,3,4,5,6,7,8,9)) # 45