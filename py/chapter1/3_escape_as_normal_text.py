# suppose you need below output
# output :  Line A \n Line B

# there are two ways to achieve this

##### way 1
print('Line A \\n Line B') # using backspace escape sequence

#### way 2
print(r"Line A \n Line B") # r is used to define RAW STRING 

# Now say you need to print below output 
# output :  \" \'

# in order to solve this lets break this problem
# \\   --- this will give you \ as output
# \'   --- this will give you ' as output

print("\\\" \\\'")