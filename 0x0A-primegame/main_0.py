#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(3, [4, 5, 1])))

print("Winner: {}".format(isWinner(2, [10, 7])))
print("Winner: {}".format(isWinner(4, [8, 11, 13, 15])))

print("Winner: {}".format(isWinner(3, [17, 20, 23])))
print("Winner: {}".format(isWinner(2, [2, 3])))
