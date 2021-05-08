"""
https://leetcode.com/problems/coin-change/

This was brought to class on May 3rd to introduce Dynamic Programming. Refer to the slides of that day.
"""
from typing import List


class Solution:
    """
    This solution has been accepted by LeetCode. It uses the Bottom Up approach of Dynamic Programming.
    """

    def coinChange(self, coins: List[int], amount: int) -> int:

        # This is an optional step. It appears that all the list of coins provided by the LeetCode test cases are
        # already sorted
        # coins.sort()

        df = [[-1 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]

        # When no change is needed, set the coins needed as zero
        for i in range(1, len(coins) + 1):
            df[i][0] = 0

        # The first row gets a value for all values of change needed, except when no change is needed
        for i in range(1, len(df[0])):
            df[0][i] = float('inf')

        # Fill out one row at a time, based on the previous row
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                # If you are at a column which is less than the value of the current coin
                if j < coins[i - 1]:
                    df[i][j] = df[i - 1][j]
                # else apply the formula: dp[i,j] = min(dp[i,j-c]+1, dp[i-1,j])
                else:
                    df[i][j] = min(df[i][j - coins[i - 1]] + 1, df[i - 1][j])

        num_of_coins = df[len(coins)][amount]
        num_of_coins = -1 if num_of_coins == float('inf') else num_of_coins

        return num_of_coins


## Coin change using N size array


class Solution2:
    def coinChange(self, coins, amount: int) -> int:
        df = [float("inf") for _ in range(amount + 1)]
        df[0] = 0

        for i in range(1, len(df)):
            minimize = [df[i - coin] + 1 for coin in coins if coin <= i]
            minimize.append(df[i])
            df[i] = min(minimize)

        return df[amount]


print(Solution2().coinChange([1], 10000))
print(Solution2().coinChange([1, 2, 5], 11))
