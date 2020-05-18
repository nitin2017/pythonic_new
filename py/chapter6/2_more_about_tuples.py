# looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking list inside tuple
# functions that can be used with tuples

mixed = (1,2,3,4.0)

# for loop with tuple 
for i in mixed:
    print(i)
# NOTE: - You can use while loop too

# tuple with one element
nums =(1)
words = ('word1')
print(type(nums)) #<class 'int'>
print(type(words)) #<class 'str'>
print(type(mixed)) #<class 'tuple'>

# In order to define a tuple with one element we need to use comma ',' at the end
nums = (1,)
print(type(nums)) #<class 'tuple'>

# tuple without parenthesis

alphabets = 'a','b','c'
print(type(alphabets))  #<class 'tuple'>

# tuple unpacking 
names = ('nitin','rahul','sachin')
name1 , name2 ,name3 = (names)
print(f"{name1} {name2} {name3}") # nitin rahul sachin

# list inside tuple 
my_tuple = ('a','b',[1,2,3,4,5]) # there is a list present in the tuple
my_tuple[2].pop()
print(my_tuple)  # ('a', 'b', [1, 2, 3, 4])  here we removed 5 from list present inside tuple
my_tuple[2].append(89)
print(my_tuple) # ('a', 'b', [1, 2, 3, 4, 89])

# some functions with tuple
# min() , max() ,sum()
print(min(mixed)) # 1
print(max(mixed)) # 4.0
print(sum(mixed)) # 10.0