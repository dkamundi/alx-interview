#!/usr/bin/python3
"""
Code
"""


def minOperations(n):
    if n<= 1:
        return n

    # Initialize a list to keep track of the minimum operations for each index.
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i

        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + 1 // j)
                dp[i] = min(dp[i], dp[i // j] + j)

    return dp[n]
