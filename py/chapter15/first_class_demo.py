# OBJECTIVES 
# WHAT IS CLASS
# HOW TO WRITE A CLASS
# WHAT IS INIT METHOD , constructor 
# WHAT ARE ATTRIBUTES , INSTANCE VARIABLES 
# HOW TO CREATE OUR OBJECT 

class Person:
    def __init__(self,first_name,last_name,age):
        # intialize instance variable 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
    

p1 = Person('nitin','kumar',31)
p2 = Person('nidhi','choudhary',28)

print(p1.first_name)
print(p2.first_name)