# Task 2
#
# Implement a function `get_pairs(lst: List) -> List[Tuple]`
# which returns a list of tuples containing pairs of elements.
# Pairs should be formed as in the example.
# If there is only one element in the list return `None` instead.
#
# Example:
# ```python
# >>> get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]
#
# >>> get_pairs(['need', 'to', 'sleep', 'more'])
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
#
# >>> get_pairs([1])
# None
# ```

def get_pairs(my_list):
    if len(my_list) < 2:
        return     # return!! // return == return None
    else:
        new_list = []
        for i in range(len(my_list)-1):
            new_list.append((my_list[i], my_list[i + 1]))
        return new_list     # return!!


print(get_pairs(['need', 'to', 'sleep', 'more']))
