user_info  ={
    'name':'nitin',
    'age':28,
    'fav_movies':['a','b','c'],
    'fav_tunes':['p','q','r']
}

# how to add data
user_info['fav_songs'] = ['song1','song2']
print(user_info) # {'name': 'nitin', 'age': 28, 'fav_movies': ['a', 'b', 'c'], 'fav_tunes': ['p', 'q', 'r'], 'fav_songs': ['song1', 'song2']}

# pop method : in order to delete 
popped_item = user_info.pop('fav_tunes')
print(type(popped_item)) # <class 'list'>  fav_tunes was of type list
print(f"popped item is {popped_item}") # popped item is ['p', 'q', 'r']
print(user_info) # {'name': 'nitin', 'age': 28, 'fav_movies': ['a', 'b', 'c'], 'fav_songs': ['song1', 'song2']


# popitem method  --- wen u want to randomly delete a K-V 

popped_item1 = user_info.popitem()
print(type(popped_item1)) # <class 'tuple'> : this was random removal
print(f"popped item is {popped_item1}") # popped item is ('fav_songs', ['song1', 'song2'])
print(user_info) # {'name': 'nitin', 'age': 28, 'fav_movies': ['a', 'b', 'c']}

