#!/usr/bin/python3
"""
Code
"""


def minOperations(n):
    """
    returns the minimum no of operations needed
    """
    num = 0
    i = 2
    if type(n) != int or n <= 1:
        return 0
    while n != 1:
        if n % i == 0:
            n = n / i
            num = num + i
        else:
            i = i + 1
    return num
