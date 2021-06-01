# ### Task 4
#
#
# Create decorator deprecated2 to take an optional argument — a function to call instead of the original function.
#
# Example:
#
#
# def deprecated2(...
#
# @deprecated2(new_foo_bar)
# def foo_bar(a, b):
#     return a + b
#
# foo_bar(1, 2)
#
# Result:
# foo_bar is deprecated. new_foo_bar will be called instead
# 2
import logging


# затруднение в том чтобы передать необязательным параметром функцию для замены
def deprecated2(foo_bar):
    # почему, если в аргумент ставлю new_foo_bar отрабатывает как будто декоратор наоборот
    def wrapper(*args):
        logging.warning(f'{foo_bar.__name__} is deprecated. {new_foo_bar.__name__} will be called instead')
        return new_foo_bar(*args)

    return wrapper


@deprecated2  # foo_bar=deprecated2(foo_bar)
def foo_bar(*args):
    return args[-1]


def new_foo_bar(*args):
    return args[0]


print(foo_bar(1, 2, 3))
