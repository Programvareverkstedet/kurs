"""
IO is boring but useful, here is how.
"""

# Input and output from the user is easy.
a = input("Some prompt here: ")
print(a)

# Input from files are a bit more tricky

# The way taught in ITGK
f = open("file.txt")
f.close()

# The correct way


with open("file.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)

# Or even better
with open("file.txt", "r") as f:
    for line in f:
        print(line)

# Even better
with open("newFile.txt", 'w') as f:
    f.write("This is a new file\nI like it.\n")

# There are four modes of reading, r, w, a and r+