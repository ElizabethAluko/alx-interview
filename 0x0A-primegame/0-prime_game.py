#!/usr/bin/python3
"""Prime Numbers Game"""


def isWinner(x, nums):
    """Determine the winner of prime game"""

    def isPrime(number):
        """Check if a number is a prime number or not"""

        if number <= 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

    # Create a list to store the results for each round
    results = []

    for n in nums:
        # Create a table to store results for each num up to n
        dp = [False] * (n + 1)

        # Initialize the base cases
        dp[0] = False
        dp[1] = False

        # Populate the table based on prime numbers
        for i in range(2, n + 1):
            if isPrime(i):
                dp[i] = not dp[i - 1]

        # Append the result for this round to the results list
        results.append("Maria" if dp[n] else "Ben")

    # Count the number of wins for each player
    maria_wins = results.count("Maria")
    ben_wins = results.count("Ben")

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
