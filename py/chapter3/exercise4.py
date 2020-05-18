# problem
# ask user to input a number containg more than one digit
# example : 1234, 1256
# calculate 1+2+3+4 or 1+2+5+6

num = input("Enter a number with more than one digit:- ").strip()
i = 0
sum = 0
while (i<len(num)):
    sum += int(num[i])
    i += 1
print(f"SUM OF DIGITS OF {num} is {sum}")

# Enter a number with more than one digit:- 1234
# SUM OF DIGITS OF 1234 is 10