# define a function which takes a number(n)
# return a dictionary containing cubes of number from 1 to n 

# example 
# cube_finder(3)
# {1:1,2:8,3:27}


def cube_finder(n):
    d = {}
    for i in range(1,n+1):
        d[i] = i**3
    return d

input_num = int(input("Enter a number :- ").strip())
print(cube_finder(input_num))
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
