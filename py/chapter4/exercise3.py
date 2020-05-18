# define is_palindrome function that will take one word as input 
# and return true if it is palindrome else return False

# e.g 
# is_palindrome("madam") --- True
# is_palindrome("nitin") --- True
# is_palindrome("horse") --- False

user_str = input("Enter a string :- ").strip()

def is_palindrome(str):
    rev_str = str[::-1]
    return rev_str == str

print(is_palindrome(user_str))