# ### Task 2
#
# Write a decorator to cache function invocation results.
# Store pairs arg:result in a dictionary in an attribute of the function object. The function being memoized is fibonacci or factorial.
# If you choose factorial please write your own function. Do not use module math.

import logging


def dec(func):
    __dict_memo = {}

    def wrapper(n):
        result = __dict_memo.get(n)
        if result is None:
            result = func(n)
            __dict_memo[n] = result
        return result

    return wrapper


@dec  # func=dec(func)
def fact(n):
    if isinstance(n, int) and n > 0:
        factorial = 1
        # можно через функцию
        # import math
        # math.factorial(4)
        while n > 1:
            factorial *= n
            n -= 1
        return factorial
    else:
        logging.warning(f'{n} is not natural number')


print(fact(3))
print(fact(5))
print(fact(3))
