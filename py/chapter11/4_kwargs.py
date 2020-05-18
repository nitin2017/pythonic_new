# kwargs (keyboard arguement)
# **kwargs (double star operator )

# kwargs as a parameter

def func(**kwargs): # kwargs gather arguement in a dictionary
    print(kwargs) # {'first_name': 'nitin', 'last_name': 'choudhary'}
    print(type(kwargs)) # <class 'dict'>
    for k,v in kwargs.items():
        print(f"{k} : {v}")
# first_name : nitin
# last_name : choudhary
func(first_name ='nitin', last_name='choudhary')