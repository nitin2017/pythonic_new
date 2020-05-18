# list comprehension with if statement

nums = list(range(1,11))

even_nums = [i for i in nums if i%2 == 0]
print(even_nums) # [2, 4, 6, 8, 10]

odd_nums = [i for i in nums if i%2 !=0]
print(odd_nums) # [1, 3, 5, 7, 9]