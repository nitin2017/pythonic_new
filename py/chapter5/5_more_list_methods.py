# count
# sort method
# sorted function 
# reverse 
# clear
# copy 

fruits = ['orange','apple','pear','banana','kiwi','apple','banana']

print(fruits.count('apple')) # 2 number of times apple is present in list 

# In order to sort list 

fruits.sort()
print(fruits) #['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'pear'

numbers = [3,5,1,9,10]
numbers.sort()
print(numbers) # [1, 3, 5, 9, 10]

# Now in case you do not want to sort your list , instead just want to print elements of a list in sorted order

print(sorted(numbers))


# in oreder to clear uour list we use clear method

numbers.clear()
print(numbers) # [] all elements are removed 

# in order to create a copy of list 

fruits_copy = fruits.copy()
print(fruits_copy) # ['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'pear']