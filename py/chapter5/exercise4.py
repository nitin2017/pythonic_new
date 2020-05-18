# filter odd even
# define a function 
# input ----> [1,2,3,4,5,6,7]
# output ---> [[1,3,5,7],[2,4,6]]

numbers = [1,2,3,4,5,6,7]

def filter_odd_even(l):
    odd = []
    even = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    out = [odd,even]
    return out

print(filter_odd_even(numbers)) # [[1, 3, 5, 7], [2, 4, 6]]