#  ***************************** Data Structures **********************************
#  An array of sequences

# List comprehensions and generator expressions
#  A quick way to build a sequence is using a list comprehension (list comps) (if the target is a list) or a generator expression (genexps)

# Listcomps no longer leak their variables
from typing import List


x = 'my precious'
dummy = [x for x in 'ABC']
print('---------------',x)
print('====================',dummy)

x = 'ABC'
dummy = [ord(x) for x in x]
print('---------------',x)
print('====================',dummy)

# List comps and readability

# Build a list of Unicode codepoints from a string - for loop
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

#  Build a list of Unicode codepoints from a string, take two - list comps
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)

# A for loop can be used to do lots of different things
# In contrast, a listcomp is meant to do one thing only: to build a new list

# Listcomps versus map and filter

# Listcomps do everything the map and filter functions do, without the contortions of the functionally challenged Python lambda.
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c:c > 127, map(ord, symbols)))

# Cartesian products
# Listcomps can generate lists from the cartesian product of two or more iterables. The items that make up the cartesian product are tuples made 
# from items from every input iterable. The resulting list has a length equal to the lengths of the input iterables multiplied.
