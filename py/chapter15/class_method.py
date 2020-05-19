
class Person:
    count_instance= 0 # class variable 
    def __init__(self,first_name,last_name,age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age 
    @classmethod
    def count_instances(clas):
        return f"YOU HAVE CREATED {clas.count_instance} OF PERSON CLASS "

    def full_name(self): # instance methods 
        return f"{self.first_name} {self.last_name}"
    def is_above_18(self): # instance methods 
        return self.age>18 

p1 = Person('nitin','kumar',11)
p2 = Person("rahul","choudhary",28)
p3 = Person("nidhi","choudhary",25)
print(p1.full_name())
print(p1.is_above_18())
print(Person.count_instances())
