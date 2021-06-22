# ### Task 3
#
# Write a decorator to memoize functions with an arbitrary set of arguments. Note that memoization is only possible if the arguments are hashable.
# If the wrapper is called with arguments which are not hashable, then the argument should be converted or the wrapped function should just be called without caching.
# Investigate the variation of usage.

import logging


# tuple внутри с листом - неизменяемый тип?
def decorator_cache(func):
    __dict_memo = {}

    def wrapper(*args, **kwargs):
        args_hash = hash(tuple(args) + tuple([(key, items) for key, items in kwargs.items()]))
        result = __dict_memo.get(args_hash)
        if result is None:
            result = func(*args, **kwargs)
            __dict_memo[args_hash] = result
            # Логгинг принтится в конце все или в начале
            # logging.warning(f'new result is calculated')
            print('new result is calculated')  # как добавить логгинг для случая, если есть уже результат
        return result

    return wrapper


@decorator_cache
def foo(*args, **kwargs):  # foo=decorator_cache(foo)
    return len(args) + len(kwargs)


print(foo(1, 2, 3))
print(foo(1, 2, 3, k=3, c=5))
print(foo(1, 2, 3, k=3, c=5))
print(foo(1, 2, 3, k=3, c=8))
print(foo(1, 2, 3, k=3, c=5))
print(foo(1, 2, 5, 'uikj', k=3, c=5))
print(foo(1, 2, 3, k=3, c=5))
