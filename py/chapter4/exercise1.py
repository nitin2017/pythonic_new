# define a function which takes two numbers as input and return greatest of two numbers

def greater(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

a = int(input("Enter first number :- ").strip())
b = int(input("Enter second number :- ").strip())
print(greater(a,b))