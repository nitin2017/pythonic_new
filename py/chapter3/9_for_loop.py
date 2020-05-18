# for loop with range

for i in range(10): # 0 to 9
    print(f"Hello World : {i}")

for i in range(1,11):
    print(f"Hello World : {i}")

# sum from 1 to n
n = int(input("ENter a number").strip())
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)

# problem
# ask user to input a number containg more than one digit
# example : 1234, 1256
# calculate 1+2+3+4 or 1+2+5+6

num = input("Enter a number with more than one digit:- ").strip()
sum = 0
for i in range(0,len(num)):
    sum += int(num[i])
    i += 1
print(f"SUM OF DIGITS OF {num} is {sum}")

# ask a user for name 
# example : Nitin Choudhary
# print count of each words


user_name =  input("ENTER YOUR NAME :- ").strip()
temp_var = ''
for i in range(0,len(user_name)):
    if user_name[i].lower() not in temp_var:
      print(f"{user_name[i].lower()}      {user_name.lower().count(user_name[i].lower())}")
      temp_var += user_name[i].lower()
    i += 1