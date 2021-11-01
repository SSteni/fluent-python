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

# Imagine you need to produce a list of t-shirts available in two colors and three sizes. Build a cartesian product using list comprehension
colors = ['black','white']
sizes = ['S','M','L']
tshirts = [(color, size) for color in colors for size in sizes] # ------ (1)
print(tshirts)

for color in colors:
    for size in sizes:
        print((color,size))   # ------ (2)

tshirts = [(color, size) for size in sizes
                         for color in colors]  # ------- (3)
print(tshirts)

# -----(1) This generates a list of tuples arranged by color, then size.
# -----(2) Note how the resulting list is arranged as if the for loops were nested in the same order as they appear in the listcomp.
# -----(3) To get items arranged by size, then color, just rearrange the for clauses; adding a line break to the listcomp makes it easy to see how the result will be ordered.

# Pro-tip: Listcomps are a one-trick pony: they build lists. To fill-up other sequence types, a genexp is the way to go. Lets look at genexps in the context of building non-list sequences.

# Generator expressions
# To initialize tuples, arrays and other types of sequences, you could also start from a listcomp but a genexp saves memory because it yields items one by one using the iterator protocol instead of building a whole list just to feed another constructor.
# Genexps use the same syntax as listcomps, but are enclosed in parenthesis rather than brackets.

# Initializing a tuple and an array from a generator expression.
symbols = '$¢£¥€¤'
print(tuple(ord(symbol) for symbol in symbols)) # ----- (1)
import array
array.array('I', (ord(symbol) for symbol in symbols)) # ----- (2)

# -----(1) If the generator expression is the single argument in a function call, ther eis no need to duplicate the enclosing parenthesis
# -----(2) The array constructor takes two arguments, so the parenthesis around the generator expression are mandatory.

# Use a genexp with a cartesian product to print out a roster of t-shirts of two colors in three sizes. In contrast with for loop, here the 6-item list of t-shirts is
# never built in memory: the generator expression feeds the for loop producing one item at a time. If the two lists used in the cartesian product had a thousand items each, using
# a generator expression would save the expense of building a list with a million items just to feed the for loop
colors = ['black', 'white']
sizes = ['S','M','L']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

# The generator expression yields items one by one; a list with all 6 t-shirt variations is never produced in this example.

# Tuples
# Tuples are not jut immutable lists
# Tuples can be used as immutable lists and also as records with no field names. 

# Tuples as records
# Tuples hold records: each item in the tuple holds the data for one field and the position of the item gives its meaning.
lax_coordinates = (33.9425, -118.408056) # (1)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014) # (2)
traveler_ids = [('USA', '31195855'), ('BRA','CE342567'), # (3)
                ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids): # (4)
    print('%s/%s' % passport) # (5)
for country, _ in traveler_ids:  # (6)
    print(country)

# (1) Latitude and longitude of the Los Angeles International Airport
# (2) Data about Tokyo: name, year, population (millions), population change (%), area (km2)
# (3) A list of tuples in the form (country_code, passport_number)
# (4) As we iterate over the list, passport is bound to each tuple
# (5) The % formatting operator understands tuples and treats each item as a separate field.
# (6) The for loop knows how to retrieve the items of a tuple separately - this is called "unpacking". Here we are not interested in second item, so its assigned to _, a dummy variable

# Tuples work well as records because if the tuple unpacking mechanism.
