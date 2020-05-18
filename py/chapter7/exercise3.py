# user_info  ={
#     'name':'nitin',
#     'age':28,
#     'fav_movies':['a','b','c'],
#     'fav_tunes':['p','q','r']
# }

# Create above dictionary by taking user's input

user = {}
name = input("Enter your name :- ".strip())
age = int(input("Enter your age :- ".strip()))
fav_movies = input("Your fav movies:- ").split(',')
fav_songs = input("Your fav songs").split(",")

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs

for k,v in user.items():
    print(f"{k}  :   {v}")

# name  :   Nitin
# age  :   29
# fav_movies  :   ['a', 'b', 'c']
# fav_songs  :   ['p', 'q', 'r']