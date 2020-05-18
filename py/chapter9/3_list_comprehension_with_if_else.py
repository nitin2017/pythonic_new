# list comprehension with if else

nums = list(range(1,11))
#  output ---> if odd then return negative of that number if positive return square [-1,4,-3,16...]

new_list = [i**2 if(i%2 == 0) else -i for i in nums]
print(new_list) # [-1, 4, -3, 16, -5, 36, -7, 64, -9, 100]