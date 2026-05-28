#!/usr/bin/python3
"""
Minimum operations module.
"""


def minOperations(n):
    """
    Return the fewest operations needed to get exactly n H characters.
    """
    if not isinstance(n, int) or n < 2:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        while n % factor == 0:
            operations += factor
            n = n // factor
        factor += 1

    return operations
