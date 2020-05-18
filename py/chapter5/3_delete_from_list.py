# common methods to delete elements from list 

fruits = ['orange','apple','pear','banana','kiwi']

# POP METHOD 
fruits.pop() # this will remove last element of list
print(fruits) # ['orange', 'apple', 'pear', 'banana']

fruits.pop(1) # this will remove element from specif position of list
print(fruits) # ['orange', 'pear', 'banana']

# DELETE OPERATOR

del fruits[1]
print(fruits) # ['orange', 'banana']

# REMOVE 
# say we do not know the position of an element in our list

fruits.remove('banana')
print(fruits) # ['orange']

# fruits.remove('mango') :-  here i am trying to remove an element from list which is not present 
# ValueError: list.remove(x): x not in list

fruits = ['orange','apple','pear','apple','kiwi']

# now we have two 'apple' named elements in list and we want to remove apple

fruits.remove('apple') # this will remove apple present at position 1 in list 
print(fruits)