def multiply_item(*args):
    # print(num)
    print(args)
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

print(multiply_item(2,3)) # 6

# now lets create a list and pass that as an arguement to function
nums = [2,3,4]
print(multiply_item(nums))
# ([2, 3, 4],)
# [2, 3, 4] Now here you can see nothing happened top out input list

print(multiply_item(*nums)) # 24 here * unpacked the items in our list