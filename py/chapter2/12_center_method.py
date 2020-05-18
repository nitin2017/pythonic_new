# center method
name = "nitin"

# required output : **nitin**

print(name.center(9,'*')) # **nitin**

# ask user to enter name and add four * on both left and right side

user_name = input("ener your name:- ").strip()
print(user_name.center(len(user_name)+8,'*'))

# ener your name:- nitin
# ****nitin****