# common elements finder function
# define a function that takes 2 lists as input and return a list
# which contains common elements of both lists 

# exampple 
# input ----> [1,2,5,8] , [1,2,7,6]
# output -----> [1,2]

l1 = [1,2,5,8]
l2 = [1,2,7,6]

def common_elements(l1,l2):
    common =[]
    for i in l1 :
        if i in l2:
            common.append(i)
    return common

print(common_elements(l1,l2)) # [1, 2]


