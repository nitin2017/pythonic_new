#strings
#collection of characters inside single quote or double quote

first_name = "Nitin"
last_name = "Choudhary"

##concatenation
full_name = first_name + " " + last_name
print(full_name)

#****** we cannot concatenate integer with string

# print(first_name + 3) TypeError: must be str, not int
print(first_name+"3")
print(first_name+str(3))

#****** we can use * operator with string
print(first_name*3) # this will print first_name three times


