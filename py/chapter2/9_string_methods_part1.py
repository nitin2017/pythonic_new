# string methods part one

name = "NiTiN cHoUdHaRy"

# len() function
print(f"Length of string name is {len(name)}") #Length of string name is 15

# lower() method
print(f"Name in lower case is {name.lower()}") # Name in lower case is nitin choudhary

# upper() method
print(f"Name in upper case is {name.upper()}") # Name in upper case is NITIN CHOUDHARY

# title() method
print(f"Name after using title method is {name.title()}") #Name after using title method is Nitin Choudhary

# count() method
N = name.count("N")
print(f"Number of time N is persent in {name} is {N}")  # Number of time N is persent in NiTiN cHoUdHaRy is 2
print(f"Number of time N is persent in {name} is {name.count('N')}")