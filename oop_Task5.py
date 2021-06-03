# Task 5
#
# Create hierarchy out of birds.
# Implement 4 classes:
# * Birds class with an attribute "name" and methods "fly" and "walk".
# * flying bird class with same attribute "name" and with the same methods.
# Implement the method "eat" which will describe it's typical ration.
# * nonflying bird class with same characteristics but which obviously will
# not have the "fly".
# Add same "eat" method but with other implementation regarding
# the swimming bird tastes.
# * a bird class which can do all of it: walk, fly, swim and eat.
# But be careful which "eat" method you inherit.
#
# Implement str() function call for each class.
#
# Example:
#
# ```python
# >>> b = Bird("Any")
# >>> b.walk()
# "Any bird can walk"
#
# p = Penguin("Penguin")
# >> p.swim()
# "Penguin bird can swim"
# >>> p.fly()
# AttributeError: 'Penguin' object has no attribute 'fly'
# >>> p.eat()
# "It eats mostly fish"
#
# c = Canary("Canary")
# >>> str(c)
# "Canary can walk and fly"
# >>> c.eat()
# "It eats mostly grains"
#
# s = SeaGull("Gull")
# >>> str(s)
# "Gull bird can walk, swim and fly"
# >>> s.eat()
# "It eats fish"
# ```
#
# Have a look at `__mro__` method of your last class.


