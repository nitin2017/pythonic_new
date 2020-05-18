def greater(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

def greatest(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    return num3

def new_greatest(num1,num2,num3):
    bigger = greater(num1,num2)
    return greater(bigger,num3)


print(new_greatest(4,7,5))