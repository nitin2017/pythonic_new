# define a function which takes list as input 
# input -----> [1,2,3,[1,2]]
# ouput -----> count number of lists prresent in out list : 2 in above list

numbers =  [1,2,3,[1,2],[3,4],5,6]

def count_list(l):
    counter = 0
    for i in l:
        if type(i) == list:
            counter += 1
    return counter

print(count_list(numbers)) # 2 
        