"""
Examples of conditionals and loops in python
"""


# This is an if statement
if True:
    print("This is true")

    print("Noe mer her...")

# And this another one
if False:
    print("This will never be printed")

# Conditions can be more complex
if 1 in [3, 2, 1, 0] and "a" != "B":
    print("This should happen even though it is needlessly complex")

# And have multiple terms
if False:
    pass
elif 2 + 2 == 5:
    five = 2 + 2
else:
    pass

# Loops also exist, the most normal is for
for x in range(1, 11):
    for y in range(1, 11):
        print(x * y, end=" \t\t")
    print()

for x in ["a", "b", "c"]:
    print(x)

# Another example
for y in ["Det", "var", "en", "gang", "en", "liste"]:
    print(y, end=" ")
print()

# Loops can have unknown length
i = 0
while i <= 10:
    print("i is <= 10")
    i += 1

# The can also be made infinite
while True:
    if i < 5:
        break
    
    print("i > 5")
    if False:
        continue
    i -= 1


# Loops can have an else clause
while True:
    break
else:
    print("This wont happens because of the break.")

for i in range(2):
    if i < -1000:
        break
else:
    print("This will be printed because the loop exits from its condition, not a break.")