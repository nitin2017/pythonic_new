# define a function that takes a list of strings 
# list containing reverse of every string

# example
# l = ['abc','pqr','xyz']
# reverse_string(l)    -----> ['cba','rqp','zyx']

l = ['abc','pqr','xyz']
def reverse_string(l):
    return [str[::-1] for str in l]

print(reverse_string(l))# ['cba', 'rqp', 'zyx']