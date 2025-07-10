"""
tuples in python
tuples are immutable,
"""

num = ( 1,2,3,4,5,6, 1000000)
print(type(num))
print(num.index(6))
print(num.count(3))        # Counts how many times 3 appears in the tuple
print(len(num))            # Returns the number of elements in the tuple
print(num[2:5])            # Slices the tuple from index 2 to 4
print(0 in num)            # Checks if 4 is in the tuple
print(max(num))            # Returns the maximum value in the tuple
print(min(num))            # Returns the minimum value in the tuple