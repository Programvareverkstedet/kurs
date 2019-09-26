"""
Some useful functions that should be mentioned
Most are used on lists
"""

# zip
for a, b in zip([1, 2, 3, 4], [3, 2, 1]):
    print("Found {} and {}, added it is {}.".format(a, b, a+b))

# map
print()
mapped = map(lambda x: 2 * x, [1, 2, 0])
print(mapped)
print(list(mapped))

print()
mapped = map(lambda a, b: a - b, [5, 3, 0], [2, 3, -5, 8])
print(mapped)
print(list(mapped))

# filter
print()
filtered = filter(lambda x: x == 3 or x is not None and x % 3 == 1, [3, 4, None, 11, 12, 13])
print(filtered)
print(list(filtered))

# div. normal utils
print()
print(len([1, 2, 3]))
print(max([1, 2, 3]))
print(min([1, 2, 3]))
print(sorted([1, 3, 2]))