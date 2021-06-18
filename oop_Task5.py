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
from abc import ABC, abstractmethod


class Bird_abstract(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Bird(Bird_abstract):
    def __init__(self, abstract_name):
        self.name = abstract_name

    def fly(self):
        print(self.name, 'can fly')

    def walk(self):
        print(self.name, 'can walk')

    def __str__(self):
        return f'{self.name} can walk and fly'


class Penguin(Bird):
    def fly(self):
        print(self.name, 'can\'t fly')

    def swim(self):
        print(self.name, 'can swim')

    def eat(self):
        print(self.name, 'eats mostly fish')

    def __str__(self):
        return f'{self.name} can walk and swim'


class Canary(Bird):
    def eat(self):
        print(self.name, "eats mostly grains")


class SeaGull(Penguin, Bird):
    def __str__(self):
        return f'{self.name} can fly, walk and swim'


b = Bird("Any")
b.walk()
# "Any bird can walk"
print(b.__str__())
b.fly()

p = Penguin("Penguin")
p.swim()
# "Penguin bird can swim"
p.fly()
# AttributeError: 'Penguin' object has no attribute 'fly'
p.eat()
# "It eats mostly fish"
p.walk()
print(p.__str__())

c = Canary("Canary")
print(str(c))
# "Canary can walk and fly"
c.eat()
# "It eats mostly grains"
c.walk()
c.fly()

s = SeaGull("Gull")
print(str(s))
# "Gull bird can walk, swim and fly"
s.eat()
# "It eats fish"
s.fly()
s.walk()
s.swim()
