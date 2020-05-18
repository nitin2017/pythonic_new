# check empty or not

name = ''

if name: ## true if string is not empty 
    print("string is not empty")
else:
    print("string is empty")

user_name = input("Enter your name :- ").strip()
if user_name:
    print(f"Your name is {user_name}")
else:
    print("You didn't typed anything")