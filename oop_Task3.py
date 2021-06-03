# Task 3
#
# Implement a function `get_shortest_word(s: str) -> str` which
# returns the longest word in the given string.
# The word can contain any symbols except whitespaces (` `, `\n`, `\t` and so on).
# If there are multiple longest words in the string with a same length
# return the word that occurs first.
#
# Example:
# ```python
#
# >>> get_shortest_word('Python is simple and effective!')
# 'effective!'
#
# >>> get_shortest_word('Any pythonista like namespaces a lot.')
# 'pythonista'
# ```

def get_shortest_word(my_str):
    my_list = my_str.split(' ')
    longest = my_list[0]

    for el in my_list:
        if len(longest) < len(el):
            longest = el
    return longest  # return!!


print(get_shortest_word('Python is simple and effective!'))
