#!/usr/bin/env python3
"""The module contains minimum operations function"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in
    exactly n H characters in a given text file containing a single
    character H.

    argument:
        n - number of H to be reproduced

    Returns:
        an integer, minimum operation.
        Or 0 if n is imporssible.

    example:
        n = 9
        H => Copy All => Paste => HH => Paste =>HHH => Copy All =>
        Paste => HHHHHH => Paste => HHHHHHHHH

        Number of operations: 6
    """

    if n <= 1:
        return 0
    elif n <= 5 or isprime(n):
        return n
    else:
        smallest_sum = float('inf')

        for divisor in range(2, int(n**0.5) + 1):
            if n % divisor == 0:
                quotient = n / divisor
                current_sum = divisor + quotient
                smallest_sum = min(smallest_sum, current_sum)

        return int(smallest_sum)

def isprime(number):
    """Check if a number is prime"""
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False

    return True
