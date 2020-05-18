# generate lists with range function
# something more about pop method
# index method 
# pass list to a function 

# generate lists with range function
numbers = list(range(1,11))
print(numbers)

# something more about pop method
# pop method returns as well
popped_item = numbers.pop()
print(popped_item) # 10

# index method
# we need to find the position of specific element
print(numbers.index(1)) # 0
numbers = [1,2,3,4,5,1]
print(numbers.index(1,3)) # search for 1 starting from 3rd position this will give 5
numbers = [1,2,3,1,4,5,1]
print(numbers.index(1,1,5)) # searcg for 1 startong from 1st pos and seacrch till 5th position , this gives 3

# pass list to a function 

def negative_list(l):
    negative =[]
    for i in l:
        negative.append(-1*i)
    return negative

print(negative_list(numbers)) # [-1, -2, -3, -1, -4, -5, -1]

