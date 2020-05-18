# ASK USER TO INPUT THREE NUMBERS AND PRINT AVERAGE OF THREE NUMBERS USING STRING FORMATTING

num1,num2,num3 = input("Enter three integers seperated by space :-").split()
avg = (int(num1)+int(num2)+int(num3))/3
print(f"Average of three numbers {num1},{num2},{num3} is {avg}")