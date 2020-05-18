# fibonacci
# 0 1 1 2 3 5 8 13 21 24

# for i in range(1,11):
#     print(i,end=" ") # this will print numbers in single line with space
def fibonacci_series(n):
    a = 0
    b = 1
    if n == 1:
        print(a,end=" ")
    elif n == 2:
        print (a, b)
    else:
      print(a,b,end = " ")
      for i in range(n-2):
          c = a+b
          a = b
          b = c
          print(b,end = " ")

num = int(input("Enter a number:- ").strip())
fibonacci_series(num)

