def add_two(num1 , num2):
    return num1+num2

a = int(input("Enter first number :- ").strip())
b = int(input("Enter second number :- ").strip())

print(add_two(a,b))

## functions practice

def last_char(name):
    return name[-1]

print(last_char("rahul"))

def odd_even(num):
    if num % 2 == 0:
        print("Number is even")
    print("Number is odd")

odd_even(5)

def is_even(num):
    return num%2 ==0

print(is_even(110))