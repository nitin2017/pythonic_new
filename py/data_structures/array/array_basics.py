import array as arr 

# CREATING PYTHON ARRAYS 
a = arr.array('d',[1.1,3.2,4.5]) # here d denotes type , d stands for double , i for integers 
print(a)

# ACCESSING PYTHON ARRAY ELEMENTS 

a =  arr.array('i',[2,4,6,8])
print("First element :", a[0])
print("Second element :", a[1])
print("Third element :", a[2])
print("Fourth element :", a[3])

# SLICING PYTHON ARRAYS 

number_list =  [2,5,62,5,42,52,48,5]
number_array =  arr.array('i',number_list)
print(number_array[2:5]) # 3rd to 5th element 
print(number_array[:-5]) # beginning to 4th 
print(number_array[5:]) # 6th to end 
print(number_array[:]) # beginning to end

# CHANGING AND ADDING ELEMENTS 

numbers  =  arr.array('i',[1,2,3,5,7,10])
# changing first element 
numbers[0] = 0
print(numbers)

# changing 3rd to 5th element 
numbers[2:5] = arr.array('i',[4,6,8])
print(numbers)

# add one item in array using append()
numbers.append(100)
print(numbers)

# add more than one item using extend()
numbers.extend([1000,2000,3000])
print(numbers)

# concatenate two arrays 
odd = arr.array('i',[1,3,5])
even  = arr.array('i',[2,4,6])

numbers = arr.array('i') # crearting an empty array of integers
numbers = odd+even 
print(numbers)

# REMOVING PYTHON ARRAY ELEMENTS 


numbers  =  arr.array('i',[1,2,3,5,7,10])

# remove() method to remove the given item 
numbers.remove(7)
print(numbers)

# pop() method to remove an item at given index 
numbers.pop(2)
print(numbers)

