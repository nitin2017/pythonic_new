# function returning function (closure)

# square
# cube 


def to_power(x):
    def calculate_power(n):
        return n**x
    return calculate_power

cube =  to_power(3)
print(cube(5))