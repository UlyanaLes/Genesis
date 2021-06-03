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
def deprecated2(new_func):
    def wrapper1(old_func):
        # почему, если в аргумент ставлю new_foo_bar отрабатывает как будто декоратор наоборот
        def wrapper(*args):
            logging.warning(f'{old_func.__name__} is deprecated. {new_func.__name__} will be called instead')
            return new_func(*args)

        return wrapper

    return wrapper1


def new_foo_bar(*args):
    return args[0]


@deprecated2(new_foo_bar)  # foo_bar=deprecated2(foo_bar) >> foo_bar=deprecated(new_foo_bar)(foo_bar)
def foo_bar(*args):
    return args[-1]


print(foo_bar(1, 2, 3))

print(deprecated2(new_foo_bar))
