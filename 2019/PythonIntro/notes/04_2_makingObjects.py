"""
Skippable if out of time, hot to define ones own objects.
"""

from __future__ import annotations

class MyVector(list):
    a = 0

    def __init__(self, dim: int, data: list):
        if dim != len(data):
            raise ValueError("Wrong dimensions in the vector!!!")
        self.dim = dim
        self.data = data
    
    def __add__(self, other: MyVector):
        if self.dim != other.dim:
            return None
        else:
            return MyVector(self.dim, [a + b for a, b in zip(self.data, other.data)])
    
    def __repr__(self):
        return "A vector of dimension {} with data:\n{}".format(self.dim, self.data)


a = MyVector(3, [1, 2, 3])
b = MyVector(3, [-1, -4, 8])

print(a)
print(b)

print(a + b)
