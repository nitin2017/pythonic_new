
class Person:
    count_instance= 0 # class variable 
    def __init__(self,first_name,last_name,age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age 
    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)
      

    @classmethod
    def count_instances(cls):
        return f"YOU HAVE CREATED {cls.count_instance} OF {cls.__name__} "

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

p3 = Person.from_string("nidhi,choudhary,25")
print(p3.full_name())
