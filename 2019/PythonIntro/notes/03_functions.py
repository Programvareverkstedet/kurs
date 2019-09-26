"""
About functions in python
"""

# Users may define their own custom functions
def temp():
    return 3

# And they may be called after they are defined
print(temp())

# They take arguments
def temp2(x, y):
    return x * y

temp2(1, 4)

# And be used lazily
def foo(y):
    return bar(y) - 1
# foo may not be called here because bar does not yet exist
# print(foo(5))
def bar(x):
    return x + 1

print(foo(5))

# Type hinting is supported (but not enforced)
def strong_typed(text: str, n: int) -> str:
    nstr = str()
    for _ in range(n):
        nstr += text
    
    return nstr
print(strong_typed("Hello world ", 4))

# Functions can take any number of arguments, optional arguments and and keyword arguments
def fancy_func(a, b="Hello", c: int = 8) -> None:
    d = a + c
    print(b, d)
fancy_func(1, c=6)

# They don't even need names
print((lambda x, y : x * y)(2, 3))

# Though lambdas are cool, they are rarely used in python
# Decorators are often cleaner
