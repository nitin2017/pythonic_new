# min and max functions

numbers  = [6,60,2]
print(min(numbers)) # 2
print(max(numbers)) # 60

# create a function which takes list as input and gives the greatest difference

def greates_diff(l):
    minima = min(l)
    maxima = max(l)
    return maxima - minima

print(greates_diff(numbers))  # 58 