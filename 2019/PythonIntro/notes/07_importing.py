"""
It is easier to reuse code and structure projects in multiple files.
"""

# We can import our own code

funcs = __import__("03_functions")

print("\n\n")
funcs.fancy_func(3)
print("\n\n")

import pandas
import numpy as np

print(np.pi)

from numpy import e
print(e)

# Libraries makes life easier, use pip for everything always