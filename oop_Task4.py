# Task 4
#
# Implement a Counter class which optionally accepts the start value and
# the counter stop value.
# If the start value is not specified the counter should begin with 0.
# If the stop value is not specified it should be counting up infinitely.
# If the counter reaches the stop value, print "Maximal value is reached."
#
# Implement to methods: "increment" and "get"
#
# /If you're familiar with Exception rising use it to display
# the "Maximal value is reached." message./
#
# Example:
# ```python
# >>> c = Counter(start=42)
# >>> c.increment()
# >>> c.get()
# 43
#
# >>> c = Counter()
# >>> c.increment()
# >>> c.get()
# 1
# >>> c.increment()
# >>> c.get()
# 2
#
# >>> c = Counter(start=42, stop=43)
# >>> c.increment()
# >>> c.get()
# 43
# >>> c.increment()
# Maximal value is reached.
# >>> c.get()
# 43
# ```
import logging

class Counter:
    def __init__(self, start=0, stop=None):
        self.__value = start   # __ для запрета редактирования внутренних атрибутов ( _ все еще могу получить из вне)
        self.__stop = stop

    def get(self):
        return self.__value

    def increment(self):
        if self.__value is not None and self.__value == self.__stop:  # сравнить с None в первую очередь
            print('Maximal value is reached.')
        else:
            self.__value += 1


c = Counter(start=42)
c.increment()
print(c.get())
# 43

c = Counter()
c.increment()
print(c.get())
# 1
c.increment()
print(c.get())
# 2

c = Counter(start=42, stop=43)
c.increment()
print(c.get())
# 43
c.increment()
# Maximal value is reached.
print(c.get())
# 43
