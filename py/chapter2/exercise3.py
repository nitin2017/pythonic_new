# take two comman seperated inputs from user
# 1) user's name
# 2) a single character

# output 2 
# 1) user's name length
# 2) count the characters that user inputed 

name,search = input("Please enter comma seperated your name and character you want to count in name :").split(",")
print(f"Length of {name} is {len(name.strip())}")
print(f"Number of times {search.strip()} present in {name} is {name.strip().lower().count(search.strip().lower())}")

# Please enter comma seperated your name and character you want to count in name :Nitin,n
# Length of Nitin is 5
# Number of times n present in Nitin is 2