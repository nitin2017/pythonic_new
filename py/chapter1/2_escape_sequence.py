# In print function we learned that :- 
# we cannot define 'single quote' inside 'single quote'
# OR
# "double quotes" inside "double quotes"
# In order to deal such situations we use escape sequences 

print("Hello \"world\" world") # this will work now \" is a double quote escape                                   character

# we have various escape sequence 
#       \'  ---- single quote
#       \"  ---- double quote
#       \\  ---- backslash
#       \n  ---- new line
#       \t  ---- tab
#       \b  ---- backspace 

print ('I\'m Nitin')  # this is single quote escape sequence

print("Line A")
print("Line B")
print("Line A\nLine B") # example of new line escape sequence

print("Name\tNitin") # example of escape tab sequence

print('this is \ backslash') # this will work with no problem
#print('this is backslash \') # SyntaxError: EOL while scanning string literal
print('this is backslash \\') # example of \\ backslash escape sequence
print('this is backslash \\\\') # double backslash

print('Hell\blo World\bd') ## useless but example of backspace escape sequence



