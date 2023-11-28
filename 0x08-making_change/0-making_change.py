#!/usr/bin/python3
"""
Module returns the fewest number of coins
needed to meet a given amount total.
"""


def makeChage(coins, total) -> int:
    """
    Returns the fewest number of coins
    needed to meet a given amount total.
    Args::
        coins (List): list of coins
        total (int)
    """

    if total <= 0:
        return 0

    number_of_coins = 0
    cents = 0

    coins = sorted(coins, reverse=True)

    for coin in coins:
        while cents + coin <= total:
            cents += coin
            number_of_coins += 1
        if cents == total:
            return number_of_coins
    return -1
