# ENCAPSULATION
# ABSTRACTION
# SOME SPECIAL NAMING CONVENTION
# NAME MANGLING __name (not a convention)

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.__price=price
    def make_a_call(self,phone_number):
        print(f"calling {phone_number}")
    def full_name(self):
        print (f"{self.brand} {self.full_name}")
    def send_message():
        pass 
    
# _name -- convention for private name 
# __name__ -- dunder/magic methos 

phone1 = Phone('nokia','1100',1000)
print(phone1.__dict__) # {'brand': 'nokia', 'model_name': '1100', '_Phone__price': 1000}