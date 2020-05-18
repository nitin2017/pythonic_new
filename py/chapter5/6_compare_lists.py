# compare lists 
# == , is

fruits1 = ['orange','apple','pear']
fruits2 = ['banana','kiwi','apple','banana']
fruits3 = ['orange','apple','pear']

#  == method compares the element of list
print(fruits1==fruits2) # False
print(fruits1==fruits3) # True

# is keyword compares object and this will return false as both are present at different memory position
print(fruits1 is fruits3) # False
