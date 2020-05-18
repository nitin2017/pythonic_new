# Q . Whar are dictionaries
# A.  Unordered collection of data in key:value pairs 

# how to create dictionaries
user = {'name':'Nitin','age':28}
print(user)
print(type(user))
# {'name': 'Nitin', 'age': 28}
# <class 'dict'>

# second method to create dictionaries
user1 = dict(name='Nitin',age=28)
print(user1)
print(type(user1))
# {'name': 'Nitin', 'age': 28}
# <class 'dict'>

# how to access data from dictionary
# there is no indexing because of unordered collection
print(user['name']) # Nitin

# which type of data can be stored in dictionary
# anything
# numbers , strings , list , dictionary

user_info ={
    'name' : 'Nitin',
    'age' : 24,
    'fav_movies': ['a','b','c'],
    'fav_tunes' : ['p','q','r']
}

print(user_info)
print(user_info['fav_movies'])
# {'name': 'Nitin', 'age': 24, 'fav_movies': ['a', 'b', 'c'], 'fav_tunes': ['p', 'q', 'r']}
# ['a', 'b', 'c']

# disctionary inside dictionary
users = {
    'user1':{
        'name':'Nitin',
        'age':'24'
    },
    'user2':{
        'name':'sachin',
        'age':19
    }
}

print(users)
print(users['user1']['name'])
# {'user1': {'name': 'Nitin', 'age': '24'}, 'user2': {'name': 'sachin', 'age': 19}}
# Nitin

# how to add data to empty dictionary

user_info2 ={}
user_info2['name'] = 'rahul'
print(user_info2)
# {'name': 'rahul'}