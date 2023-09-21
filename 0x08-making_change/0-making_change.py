#!/usr/bin/python3
"""Makechange Module"""


def makeChange(coins, total):
    """Returns the fewest number of coins needed to meet a given
    amount of total

    args:
        coins (an integer greater than zero) - A list of values
        of the available coins.

        total - The amount you need to meet.

    Returns:
        fewest number of coins needed to meet total.
        returns 0 - if total is 0 or less.
        returns -1 - if total can not be met
    """
    if total <= 0:
        return 0

    # Initialize a list to store the min number of coins for each
    # total from 0 to 'total'.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # It takes 0 coins to make a total of 0

    # Iterate through each coin denomination
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1  # No combination of coins can make the total
    else:
        return dp[total]  # Minimum number of coins to make the total
