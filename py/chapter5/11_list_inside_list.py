# list inside list

matrix = [[1,2,3],[4,5,6],[7,8,9]] ## this is known as 2D list

# 3 items opf type list are present in matrix

print(matrix[0]) # [1, 2, 3]

# for loop on matrix list

for i in matrix:
    print(i)
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

for sublist in matrix:
    for i in sublist:
        print(i)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# access 5 present in matrix
print(matrix[1][1])
print(matrix[2][0])

print(type(matrix)) # <class 'list'>