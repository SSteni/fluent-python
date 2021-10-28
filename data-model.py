# Data Model is description of Python as a framework. 
# It formalizes the interfaces of the building blocks of the language itself such as sequences, iterators, functions, classes, context managers and so on.
# The Python interpreter invokes special methods to perform basic object operations, often triggered by special syntax.
# This special method names are always spelled with leading and trailing double underscores
# The special methods are also known as dunder methods

#  A Pythonic Card Deck - We are going to implement two special methods, __getitem__ and __len__

from _typeshed import Self
import collections

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    # print(ranks)
    suits = 'spades diamonds clubs hearts'.split()
    # print(suits)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]    

beer_card = Card('7', 'diamonds')
# print(beer_card)

deck = FrenchDeck()
# print(len(deck))

# print(deck[0])
# print(deck[1])

# Get a random item from a sequence
from random import choice
print(choice(deck))

# top 3 cards from a brand new deck
print(deck[:3])
# pick just the aces by starting on index 12 and skipping 13 cards at a time
print(deck[12::13])

# Just by implementing the __getitem__ special method, our deck is also iterable
for card in deck:
    print(card)

# The deck can also be iterated in reverse
for card in reversed(deck):
    print(card)

# Iteration is often implicit.
# If a collection has no __contains__ method, the in operator does a sequential scan. 
print(Card('Q', 'hearts') in deck)

# Function that ranks cards 

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# Given spades_high, we can now list our deck in order of increasing rank:

for card in sorted(deck, key=spades_high):
    print(card)

# By implementing the special methods __len__ and __getitem__ our FrenchDeck behaves like a standard Python sequence, allowing
# it to benefit from core language features - like iteration and slicing - and from the standard library - random.choice, reversed and sorted

# How special methods are used
# Special methods are meant to be called by the Python interpreter and not by you. You dont write my_object.__len__(). You write len(my_object) and, if my_object is an instance of a user
# defined class, then Python calls the __len__ instance method you implemented.
# Normally, your code should not have many direct calls to special methods. Unless you are doing a lot of metaprogramming, you should be implementing special methods more often than invoking them explicitly. The only special method that is frequently
# called by user code directly is __init__, to invoke the initializer of the superclass in your own __init__ implementation.

# Vector Class implementing operations through special methods for __repr__, __abs__, __add__ and __mul__
from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

# Testing
v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)

v = Vector(3, 4)
print(abs(v))

print(v * 3)
print(abs(v * 3))

# A faster implementation of Vector .__bool__ is:
def __bool__(self):
    return bool(self.x or self.y)

