"""
In python, all things are object.
This means that all functionality associated with a piece of data is stored with the data.
"""

# Making a new integer with the int constructor:

a = int(5)
b = int(4)

# Adding them together
print(a + b)
# Or without the read macro and function call:
print(a.__add__(b).__repr__())

# The most useful method ever
print("Hello {}\nI am {}".format("people who are still here", "the master of the .format method on strings"))