
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.__price=max(price,0) 

    def make_a_call(self,phone_number):
        return (f"calling {phone_number}")

    def full_name(self):
        return  (f"{self.brand} {self.model_name}")


class SmartPhone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        #Phone.__init__(self,brand,model_name,price)
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera  

phone1 = Phone('nokia','1100',1000)
smartphone1 = SmartPhone('one plus','5',30000,'6 GB','64 GB','20 MP')
print(phone1.full_name())
print(smartphone1.full_name())