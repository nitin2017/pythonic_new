# print number from 1 to 10 and break the loop if number = 5

for i in range (1,11):
    if i == 5:
        break
    print(i)

# 1
# 2
# 3
# 4

# ********************************************************

for i in range (1,11):
    if i % 2 == 0:
        continue
    print(i) 

# 1
# 3
# 5
# 7
# 9