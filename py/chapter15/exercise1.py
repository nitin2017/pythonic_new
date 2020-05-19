# create a laptop class with attributes like brand_name , model_name , price 
# create two objects/instance of your laptop class 

class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name =  brand_name
        self.model_name  = model_name 
        self.price = price

laptop1  = Laptop('sony','viao',55000)
laptop2  = Laptop('hp','xyz',35000)
