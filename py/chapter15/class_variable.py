# class variable 
# circle 
# area 
# circumference 

class Circle:
    pi =3.14
    def __init__(self,radius):
        self.radius = radius
    def calc_circum(self):
        return 2*Circle.pi*self.radius
    def calc_area(self):
        return Circle.pi*self.radius*self.radius

c1 = Circle(4)
c2 = Circle(5)
print(c1.calc_circum())
print(c1.calc_area())
print(c1.__dict__) # {'radius': 4}
print(c2.__dict__) # {'radius': 5}