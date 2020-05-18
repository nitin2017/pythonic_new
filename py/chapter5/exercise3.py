# # define a function that take list of words as arguement 
# # and return list with reverse of every element in that list

# example
# ['abc','pqr','xyz']  ------> ['cba','rqp','zyx']

my_list = ['abc','pqr','xyz']

def reverse_element(l):
    reverse = []
    for i in range(0,len(l)):
        var = l[i]
        reverse.append(var[::-1])
    return reverse

print(reverse_element(my_list)) # ['cba', 'rqp', 'zyx']