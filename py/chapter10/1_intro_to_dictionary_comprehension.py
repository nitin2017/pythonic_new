# dictionary comprehension
# square = {1:1,2:4,3:9}

square = {f"square of {num} is":num**2 for num in range(1,11)}
print(square) #{'square of 1 is': 1, 'square of 2 is': 4, 'square of 3 is': 9, 'square of 4 is': 16, 'square of 5 is': 25, 'square of 6 is': 36, 'square of 7 is': 49, 'square of 8 is': 64, 'square of 9 is': 81, 'square of 10 is': 100}

for k,v in square.items():
    print(f"{k} : {v}")

# count characters in string

word_count = {char:"nitin".count(char) for char in "nitin"}
for k,v in word_count.items():
    print(f"{k} : {v}")
# n : 2
# i : 2
# t : 1
