"""
Good built in data structures is among the most important things in a good language.
Python has several.
"""

# The list
a = list()
a = []
a = [1, 3, 4, 5 ,6]

# They act like expected
for item in a:
    print(item)
print("\n\n")

# They can contain different types
b = [1, "Hello", a, 3.14, lambda a : a + 1]

for item in b:
    print(item)

# And be mutated
a.append(8)
a.extend(["Hello", "World"])
a[1] = 100

print(a)

print(a[:5])

print("\n\n\n")

# They are objects and can be inherited as such
print(dir(a))

class MyList(list):
    def __repr__(self):
        return "This is a useless representation"
    #pass

b = MyList(a)
print(b)


# The dictionary
# A mutable fast type agnostic hashed map
a = dict()
a = {}
a = {2: "Hello world", 3: b, 8: 6.12345}
# Note that all keys must be hashable
# a[["Not working"]] = 3
a[3] = ["This might work", "I think"]
print(a)

# They can be mutated
a[2] = 5
del a[3]

print(a)

# The keys and values can be easily red
print(a.keys())
print(a.values())


# The set

# They act like keys in dictionaries, assuming this makes using them easy
a = set()
a = {'apple', 'orange', 'apple', 'banana', 3, 3, 3, 3, 3}
print(a)

# Lists and set can be made from each other
a = [1, 2, 3, 2, 1, 2, 3, 2, 1]
b = set(a)
c = list(b)
print(a)
print(b)
print(c)
