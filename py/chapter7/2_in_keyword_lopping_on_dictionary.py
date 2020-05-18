# in keyword and iterations on dictionary

user_info  ={
    'name':'nitin',
    'age':28,
    'fav_movies':['a','b','c'],
    'fav_tunes':['p','q','r']
}

# check if key exists in dictionary
if 'name' in user_info:
    print("present")
else:
    print("not present")

if 'namess' in user_info:
    print("present")
else:
    print("not present")

# check if value exists in dictionary
if 'nitin' in user_info.values():
    print("present")
else:
    print("not present")

if ['a','b','c'] in user_info.values():
    print("present")
else:
    print("not present")

    
# loops in dictionaries

for i in user_info: # this will rpint all the keys 
    print(i)

for i in user_info.values(): # this will print all the values
    print(i)

# values method
user_info_values = user_info.values()
print(user_info_values)
#dict_values(['nitin', 28, ['a', 'b', 'c'], ['p', 'q', 'r']])
print(type(user_info_values))
# <class 'dict_values'>

# keys method 

user_info_keys = user_info.keys()
print(user_info_keys)
#dict_keys(['name', 'age', 'fav_movies', 'fav_tunes'])
print(type(user_info_keys))
# <class 'dict_keys'>

## loop on values with help of keys

for i in user_info:
    print(user_info[i])
# nitin
# 28
# ['a', 'b', 'c']
# ['p', 'q', 'r']

### ITEM METHOD

user_items = user_info.items() # this returns evry K-V pair as tuple
print(user_items)
print(type(user_items))
# dict_items([('name', 'nitin'), ('age', 28), ('fav_movies', ['a', 'b', 'c']), ('fav_tunes', ['p', 'q', 'r'])])
# <class 'dict_items'> 

for key , value in user_info.items(): # here tuple unpacking is happening 
    print(f"KEY IS {key} AND VALUE IS {value}")
# KEY IS name AND VALUE IS nitin
# KEY IS age AND VALUE IS 28
# KEY IS fav_movies AND VALUE IS ['a', 'b', 'c']
# KEY IS fav_tunes AND VALUE IS ['p', 'q', 'r']