# ask a user for name 
# example : Nitin Choudhary
# print count of each words


user_name =  input("ENTER YOUR NAME :- ").strip()
temp_var = ''
i = 0
while(i<len(user_name)):
    if user_name[i].lower() not in temp_var:
      print(f"{user_name[i].lower()}      {user_name.lower().count(user_name[i].lower())}")
      temp_var += user_name[i].lower()
    i += 1

