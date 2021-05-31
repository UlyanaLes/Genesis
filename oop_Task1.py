# Task 1
#
# Implement the decorator function, which helps to count how many times
# the function has occurred.
#
# *NOTE:* NOT able to use global variables.
#
# Implementation example:
# ```python
# def dec(foo):
#   ...
#
# @dec
# def foo(): pass
#
# foo()
# foo()
# foo()
# foo()
# r = foo()
# print(r)
# >>> 5
# ```

def dec(foo):
    def wrapper():
        wrapper.count += 1
        foo()
        return wrapper.count

    wrapper.count = 0
    return wrapper


@dec    # foo=dec(foo)
def foo():
    pass

@dec
def foo2():
    pass

foo()
foo()
foo()
foo()
r = foo()
print(r)

foo2()
print(foo2())
