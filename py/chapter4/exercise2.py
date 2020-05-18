# define a function which takes three numbers as input and return greatest of two numbers

def greatest(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    return num3

a = int(input("Enter first number :- ").strip())
b = int(input("Enter second number :- ").strip())
c = int(input("Enter third number :- ").strip())

print(f"Greatest amongst three numners {a},{b},{c} is {greatest(a,b,c)}")