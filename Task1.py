# ### Task 1
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments
#  (your wrapper function should take both *args and **kwargs and print them both):
#
#
# >>> @logged
#     def func(*args):
#     return 3 + len(args)
#
# >>> func(4, 4, 4)
#
# you called func(4, 4, 4)
# it returned 6
# 6
import logging


def logged(func):
    def wrapper(*args, **kwargs):
        # почему автоматически в лог доставляются скобки круглые? // нужно распаковать List и dict
        func_result = func(*args, **kwargs)
        logging.warning(f"""you called {func.__name__} {*args,*[i for i in kwargs.values()]}  
        it returned {func_result}""")  # как сделать так чтобы func не вызывать дыважды? просто сохранить резутьтат в переменную?
        return func_result

    return wrapper


@logged  # func=logged(func)
def foo(*args, **kwargs):
    return 3 + len(args) + len(kwargs)


print(foo(1, 2, 3, a=7, b=4))
