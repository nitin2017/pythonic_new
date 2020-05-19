
def square(a):
    return a**2

s = square(7)
print(s)

s1 = square
# Now we can treat a variables s1 as function square

print(s1(7))
print(s1.__name__) # square 

print(s1)     # <function square at 0x0000025194AC2F28>
print(square) # <function square at 0x0000025194AC2F28>