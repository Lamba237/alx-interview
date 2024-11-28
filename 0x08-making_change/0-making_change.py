#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed
    to meet a given amount total.

    Args:
    coins: list of value of coins in my possession
    total: amount of money needed to meet a given amount of total

    Return: fewest number of coins needed
    """

    if total <= 0:
        return 0

    # initiate the dp array with a value greater
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
