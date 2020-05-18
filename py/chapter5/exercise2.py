# define a function which will take a list as arguement and this function will return a reversed list 

# example
# [1,2,3,4]  -----> [4,3,2,1]
# ['word1,'word2']  -----> ['word2','word1']

l1 = [1,2,3,4]
l2 = ['word1','word2','word3']

# solution 1
def reverse_list(l):
    return l[::-1]

# solution 2
def reverse_list_1(l):
    reverse = []
    for i in range(len(l)-1,-1,-1):
        reverse.append(l[i])
    return reverse

# solution 3
def reverse_list_2(l):
    reverse = l.reverse()
    return reverse

# solution 4
def reverse_list_3(l):
    reverse = []
    for i in range(0,len(l)):
        reverse.append(l.pop())
    return reverse

print(reverse_list(l1)) # [4, 3, 2, 1]
print(reverse_list_1(l2))    # ['word3', 'word2', 'word1']
print(reverse_list_1(l1)) # [4, 3, 2, 1]
print(reverse_list_3(l2)) #['word3', 'word2', 'word1']
