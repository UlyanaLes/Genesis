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