# in keyword in sets and for loop

s = {'a','b','c','d'}

# in keyword to check if item is present in list or not 

if 'a' in s:
    print("present")
else:
    print("not present")


# for loop

for item in s:
    print(item)

# set maths 

s1 = {1,2,3,4}
s2 = {3,4,5,6}

# union

print(s1.union(s2)) # {1, 2, 3, 4, 5, 6}
print(s1|s2) # {1, 2, 3, 4, 5, 6}

# intersection

print(s1.intersection(s2)) # {3, 4}
print(s1 & s2) # {3, 4}