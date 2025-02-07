#Python Variables

x = 5 # int
y = "PP2" #str

print(x)
print(y)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))

#Assign Multiple Values

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Note: Make sure the number of variables matches the number of values, or else you will get an error.

#And you can assign the same value to multiple variables in one line:

x = y = z = "Apple"
print(x)
print(y)
print(z)

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#The Python print() function is often used to output variables.

x = "Python is awesome"
print(x)

#In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#You can also use the + operator to output multiple variables:

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

#Global variables 

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

