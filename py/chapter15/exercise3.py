class Person:
    count_instance =0
    def __init__(self,first_name,last_name,age):
        Person.count_instance += 1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

p1 = Person("nitin","kumar",31)
p2 = Person("rahul","choudhary",28)
p3 = Person("nidhi","choudhary",25)
print(Person.count_instance)
