user_info  ={
    'name':'nitin',
    'age':28,
    'fav_movies':['a','b','c'],
    'fav_tunes':['p','q','r']
}

## another dictionary
more_info = {
    'name':'abhi',
    'state':'Haryana',
    'hobbies':['coding','reading','movies']
}

# we want to add more info dict content in user info

user_info.update(more_info)
print(user_info)
# {'name': 'abhi', 'age': 28, 'fav_movies': ['a', 'b', 'c'], 'fav_tunes': ['p', 'q', 'r'], 'state': 'Haryana', 'hobbies': ['coding', 'reading', 'movies']}

# here 'name' got updated 
