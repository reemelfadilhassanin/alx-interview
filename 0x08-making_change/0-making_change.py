#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a total amount.
"""


def makeChange(coins, total):
    # If total is less than or equal to 0, return 0
    if total <= 0:
        return 0

    # Initialize a dp array with infinity (a large value)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Iterate over each coin
    for coin in coins:
        # Update dp array for all amounts from coin to total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be formed
    return dp[total] if dp[total] != float('inf') else -1
