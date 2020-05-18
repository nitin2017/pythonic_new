def user_info(first_name , last_name , age=23):  # age =23 is default parameter 
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"Your age is {age}")

user_info("nitin","choudhary") # here age will remain 23
user_info("nitin","choudhary",28) # here age will get overrirde with value 28

# Now you have to make last arguement as default , u cannot keep in between arguement as default

def user_info1(first_name , last_name='unknown' , age):
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"Your age is {age}")

user_info1("Nitin",28) # SyntaxError: non-default argument follows default argument