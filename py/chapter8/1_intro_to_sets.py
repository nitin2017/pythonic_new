# set data type
# unordered collection of unique items

s = {1,2,3,2}
print(type(s)) # <class 'set'>
print(s) # {1, 2, 3} duplicate 2 removed

l = [1,2,3,4,5,5,5,5,6,7,7,8]
# remove duplicate
s2 = list(set(l))  # converted list to set and then back to list
print(s2) #[1, 2, 3, 4, 5, 6, 7, 8] removed duplicates

## some methods of set

s ={1,2,3}
s.add(4)
print(s) # {1, 2, 3, 4}

s.remove(3)
print(s) # {1, 2, 4}
# s.remove(5) # KeyError: 5 this gives error since 5 is not present in set

# Now in order to get away from above error we use discard methods

s.discard(5)
print(s) # {1, 2, 4}

s.clear()
print(s) # set()

s ={1,2,3}

s1 = s.copy()
print(s1) # {1, 2, 3}


s = {1,1.0,2.3,'string'} # {1, 2.3, 'string'} 1.0 and 1 are same
print(s)
# WE CANNOT STORE LIST,TUPLE , DICTIONARY IN LIST
s = {1,1.0,2.3,'string',[1],{1:1}}
# print(s) # TypeError: unhashable type: 'list'
