# sum : 1 to n 

n = int(input("Enter a natural number :- ").strip())
sum = 0
i = 1
while(i<=n):
    sum += i
    i +=1
print(f"Sum of 1 to {n} is {sum}")