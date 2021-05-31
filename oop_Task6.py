# Task 6
#
# Implement a class Money to represent value and currency.
# You need to implement methods to use all basic arithmetics expressions
# (comparison, division, multiplication, addition and subtraction).
# To use this methods on different currencies implement
# an exchange_rate attribute.
# This attribute you should be able to change according
# to the currency or even delete.
#
# Example:
# ```python
# >>> usd = Money(12, "usd")
# >>> usd_t = Money(42, "usd")
# >>> usd + usd_t
# Money(54, "usd")
#
# >>> usd = Money(100, "usd")
# >>> eur = Money(42, "eur")
# >>> usd.exchange_rate = 0.89
# >>> usd - eur
# Money(47, "usd")
#
# >>> del usd.exchange_rate
# ```
#
# NOTE: Have a look at @functools.total_ordering