# way 1
name = 'nitin'
for num in range(len(name)):
    print(name[num])

# way 2
name = 'rahul'
for i in name:
    print(i)

# 1256 -> 1+2+5+6

sum = 0
num = input("ENTER A NUMBER WITH MORE THAN ONE DIGIT :- ").strip()
for i in num:
    sum += int(i)
print(f"Sum of digit of number {num} is {sum}")

# ENTER A NUMBER WITH MORE THAN ONE DIGIT :- 1256
# Sum of digit of number 1256 is 14
