# fromkeys
# we use this to create a dictionary

# d = {
#     'name'= 'unknown'
#     'age' = 'unknown'
# }

# In order to create above dictionary
d = dict.fromkeys(['name','age','height'],'unknown')
print(d) # {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}

# we can use tuple as well
d = dict.fromkeys(('name','age','height'),'unknown')
print(d) # {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'

d = dict.fromkeys(('abc'),'unknown')
print(d) # {'a': 'unknown', 'b': 'unknown', 'c': 'unknown'}

d = dict.fromkeys(range(1,11),'unknown')
print(d)
# {1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown', 6: 'unknown', 7: 'unknown', 8: 'unknown', 9: 'unknown', 10: 'unknown'}

d = dict.fromkeys(['name','age'],['unknown','unknown'])
print(d) # {'name': ['unknown', 'unknown'], 'age': ['unknown', 'unknown']}


########### GET METHOD : better way to access keys 
d = dict.fromkeys(['name','age','height'],'unknown')
# print(d['names']) # KeyError: 'names this will give error
print(d.get('name')) # unknown
print(d.get('names')) # None : this will not give error

if d.get('name'): ### If  None then False else True
    print("Present")
else:
    print("Not Present")

### copy method 
# d1 = d doesn't create different dictionary we have to use copy method
d1 = d.copy() # {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}
print(d1)

### clear
d.clear()
print(d) # {}

#### more about get methods , two same keys in dict

user = {'name':'nitin','age':28}
print(user.get('name')) # nitin , name was present so value returned
print(user.get('names')) # None , none is returned since it was not present 
# Now consider we don't want None as return type , we want some defualt value

print(user.get('names','not_found')) # not_found

user = {'name':'nitin','age':28,'age':34} # duplicate key in dictionary
print(user) # {'name': 'nitin', 'age': 34} age value was overridden



