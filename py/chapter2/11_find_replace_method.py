# replace() method
# find() method

string  = "she is beautiful and she is good dancer"

# replace all spaces with underscore
print(string.replace(" ","_")) # she_is_beautiful_and_she_is_good_dancer

#replace 'is' with 'was'
print(string.replace("is","was"))  # she was beautiful and she was good dancer

print(string.replace("is","was",1)) # she was beautiful and she is good dancer

# find the position of 'is' in  string

print(string.find('is')) # 4

string  = "is she is beautiful and she is good dancer"

# find starting from specific position
print(string.find('is',1)) # 7

# now consider we don't know the occurence position of first 'is' and we need to find the position of second 'is'
string  = "she is beautiful and she is good dancer"
pos = string.find('is')
print(string.find('is',pos+1))  # 25