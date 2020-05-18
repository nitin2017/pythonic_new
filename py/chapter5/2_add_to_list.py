# how to add item to your list

fruits = ['grapes','apple']

# APPEND METHOD 
#  now you want to add another fruit in list

fruits.append('mango') # append will add item at last in your list
print(fruits) # ['grapes', 'apple', 'mango']

fruits = [] 
fruits.append('mango')
fruits.append('grapes')
print(fruits) # ['mango', 'grapes']

# INSERT METHOD 
fruits1 = ['mango','orange']
# In order to add item at any specific position
fruits1.insert(1,'grapes') 
print(fruits1) # ['mango', 'grapes', 'orange']

 # In case i try to add element to list which dosen't exist it will add element at end of list
fruits1.insert(20,'cherry')
print(fruits1) # ['mango', 'grapes', 'orange', 'cherry']


# Join (concatenate two lists)
fruits2 = ['apple','guava','cherry']
fruits_concat = fruits1 + fruits2
print(fruits_concat) #['mango', 'grapes', 'orange', 'cherry', 'apple', 'guava', 'cherry'] here cherry will repeat as it was prersent in both the list

# EXTEND METHOD 
# in above example we created new list(fruits_concat) by adding elements of two different lists(fruits1,fruits2)
# now in case we want to add elemnts of fruits2 to list fruits1 we use extend method

fruits1.extend(fruits2)
print(fruits1) # ['mango', 'grapes', 'orange', 'cherry', 'apple', 'guava', 'cherry']

# now say you want to add list (fruits2) as an element itself in list1(fruits1) we use append method

fruits1.append(fruits2)
print(fruits1) # ['mango', 'grapes', 'orange', 'cherry', 'apple', 'guava', 'cherry', ['apple', 'guava', 'cherry']]


