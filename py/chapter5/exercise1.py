# define a function which will take list containing numbers as input 
# and return list containing square of every element

# example
# numbers = [1,2,3,4,5]
# square_list(numbers) -------> return ------> [1,4,9,16,25]

numbers = [1,2,3,4,5]
def square_list(l):
    square_list = []
    for i in l:
        square_list.append(i**2)
    return square_list

print(square_list(numbers))