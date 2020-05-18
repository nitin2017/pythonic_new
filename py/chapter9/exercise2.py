# num to string
# define a function

# example
# input -------> [True,False,[1,2,3],1,1.0,3]
# output ------> ['1','1.0','3']

l = [True,False,[1,2,3],1,1.0,3]
def num_to_string(l):
    return [str(item) for item in l if (type(item)==int or type(item) == float)]

print(num_to_string(l)) # ['1', '1.0', '3']
