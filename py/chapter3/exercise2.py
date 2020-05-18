# WATCH movie 
# ASK USER's NAME AND AGE
# if user's name starts with ('a' or 'A') and age is above 10 then 
# print you can watch movie
# else sorry you can't watch movie

name,age = input("ENTER YOUR NAME AND AGE:- ").strip().split(",")
if name[0].strip().lower() == 'a' and int(age) > 10 :
    print("You can watch movie")
else:
    print("Sorry , You cannot watch movie")