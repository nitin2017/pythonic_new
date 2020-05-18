# list comprehension
# with the helo of list comprehension we can create list in one line 

# create a list of squares from 1 to 10

squares = [i**2 for i in range(1,11)]
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# create a list of negative numbers from -1 to -10

negative = [-i for i in range(1,11)]
print(negative) # [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

## example 3
names = ['nitin','sachin','rahul','abhi']
# output should be first alphabet of each string in list ----> ['n','s','r','a']

first = [name[0] for name in names]
print(first) # ['n', 's', 'r', 'a']