# data structures
# list : ordered collection of items 
# we can store anything in lists int , float , string

numbers = [1,2,3,4,5]
print(numbers)
print(numbers[1]) # list position starts from 0 , here we are accessing second element of list

words = ['word1','word2','word3','word4','word5']
print(words)
print(words[:2]) ## slicing similar to string slicing 

mixed  = [1,2,3,4,5,"six","seven",2.3,None] # we can store mixed elements in list
print(mixed)
print(mixed[-1]) # negative address

# changing data in list 
mixed[1] = 'two'
print(mixed)

mixed[1:] = 'two'
print(mixed) # [1, 't', 'w', 'o']

mixed[1:] = ['two','three','four']
print(mixed) # [1, 'two', 'three', 'four']
