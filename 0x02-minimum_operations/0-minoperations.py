#!/usr/bin/python3
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

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n /= divisor
        divisor += 1

    return operations
