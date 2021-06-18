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

class Money:
    # __dict_exchange = {usd: 1, eur: 0.89, byn: 2.6, rub: 100}

    def __init__(self, amount_inst, currency_inst):
        self.amount = amount_inst
        self.currency = currency_inst
        self.exchange_rate = None

    def trans_and_verify(self):
        if self.currency != 'usd':
            if hasattr(self, "exchange_rate") and self.exchange_rate is not None:
                return self.amount * self.exchange_rate
            else:
                raise TypeError('exchange_rate attribute is empty or missed')
        else:
            return self.amount

    ## проверка на тип???
    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        else:
            return Money(self.trans_and_verify() + other.trans_and_verify(), "usd")

    def __mul__(self, other):
        return Money(self.amount * other.amount, self.currency)

    def __truediv__(self, other):
        return Money(self.amount / other.amount, self.currency)

    def __sub__(self, other):
        return Money(self.amount - other.amount, self.currency)

    def __lt__(self, other):
        return self.amount < other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    def __le__(self, other):
        return self.amount <= other.amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __str__(self):
        return f'Money({self.amount},{self.currency})' + f'{" exchange_rate = " + str(self.exchange_rate) if hasattr(self, "exchange_rate") and self.exchange_rate is not None else ""}'


usd = Money(2, "usd")
usd_t = Money(5, "usd")
eur = Money(2, "eur")
eur_t = Money(7, "eur")
eur_t.exchange_rate = 2
print(usd + usd_t)
print(usd + eur_t)
print(eur + eur_t)
print(eur_t + usd)
# print(usd * usd_t)
# print(usd / usd_t)
# print(usd - usd_t)
# print(usd < usd_t)
# print(usd <= usd_t)
# print(usd > usd_t)
# print(usd >= usd_t)
# usd.exchange_rate = 0.89
# print(usd)
# del usd.exchange_rate
# print(usd)
