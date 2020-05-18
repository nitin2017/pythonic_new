number1 = 1
print(number1)
number1 = 4
print(number1)
name = "Nitin"
print(name)
name = 123  #this is dynamic programming as we change the data type of variable
print(name) 

##### RULES OF DEFINING VARIBALE

#################################RULES TO DEFINE VARIABLE################
# RULE 1 : variable cannot start with number BUT CAN USE IN BETWEEN
# 1number = 4 --- this is wrong
num1ber = 4
print(num1ber)

# RULE 2 : variable can start with letter , underscore
_name = "Nitin"
print(_name)

# RULE 3: CANNOT USE SPECIAL SYMBOL AT START OR EVEN IN BETWEEN
#  $name = "Nitin"  -- this is wrong

#######################CONVENTION########################

# if variable name has more than one word seperate it using underscore
# this is known as snale case writing
useronename = "Nitin"  # this is not correct way
user_one_name = "Nitin"  # this is correct

# camel case writing
userOneName = "Nitin"

# As per google we should use snake case writing in Python language 
# camel case is used more in Java

name,age = "Nitin",24
print("Hi "+name +" ! Your age is " + str(age))
x=y=z=1
print(x+y+z)


