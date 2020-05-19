# can we derive more than 
# multilvel inheritance 
# method resolution order
# method overriding 
# isinstance() , issubclass()

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.price=max(price,0) 

    def make_a_call(self,phone_number):
        return (f"calling {phone_number}")

    def full_name(self):
        return  (f"{self.brand} {self.model_name}")


class SmartPhone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera  
    def full_name(self):
        return   f"{self.brand} {self.model_name} and the price is  {self.price}"

class FlagshipPhone(SmartPhone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera = front_camera
    def full_name(self):
        return   f"{self.brand} {self.model_name} and the price is  {self.price} and camera is {self.front_camera}"
    

phone1 = Phone('nokia','1100',1000)
smartphone1 = SmartPhone('one plus','5',30000,'6 GB','64 GB','20 MP')
#smartphone2 = SmartPhone2('one plus','5',30000,'6 GB','64 GB','20 MP')
oneplus = FlagshipPhone('iphone 5','5',40000,'6 GB','64 GB','20 MP','5 MP')
print(phone1.full_name())
print(smartphone1.full_name())
print(oneplus.full_name())
#print(help(FlagshipPhone))
print(isinstance(smartphone1,SmartPhone)) # True
print(isinstance(smartphone1,Phone)) # True
print(issubclass(SmartPhone,Phone))


## method resolution order 

# class FlagshipPhone(SmartPhone) |  Method resolution order:
#  |      FlagshipPhone
#  |      SmartPhone
#  |      Phone
#  |      builtins.object
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  ----------------------------------------------------------------------
#  |  Methods inherited from Phone:
#  |
#  |  full_name(self)
#  |
#  |  make_a_call(self, phone_number)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors inherited from Phone:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)