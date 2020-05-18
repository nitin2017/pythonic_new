# define a function whcih takes a list of string as input
# and returns first alphabet of string as capital 

def func(l,**kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]

names = ['nitin','nidhi','rahul','abhi']
print(func(names)) # ['Nitin', 'Nidhi', 'Rahul', 'Abhi']
print(func(names,reverse_str = True)) # ['Nitin', 'Ihdin', 'Luhar', 'Ihba'