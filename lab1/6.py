'''
    Python Numbers
There are three numeric types in Python:

  int
  float
  complex
  
Variables of numeric types are created when you assign a value to them:
'''

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x = 1
y = 35656222554887711
z = -3255522

#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 1.10
y = 1.0
z = -35.59

#Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 35e3
y = 12E4
z = -87.7e100

#Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -5j

#You can convert from one type to another with the int(), float(), and complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#   Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

import random

print(random.randrange(1, 10))#Import the random module, and display a random number between 1 and 9:




