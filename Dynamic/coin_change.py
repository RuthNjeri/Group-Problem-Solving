class Solution:
    def coinChange(self, coins, amount):
        df = [[-1 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        df[0][0] = 0

        for i in range(1, len(df[0])):
            df[0][i] = float("inf")

        # coins.sort() # You may or may not need to sort
        self.dp(coins, amount, df)
        if df[len(coins)][amount] == float("inf"):
            return -1
        return df[len(coins)][amount]

    def dp(self, coins, amount, df):
        for i in range(1, len(coins) + 1):
            df[i][0] = 0
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                if j < coins[i - 1]:
                    df[i][j] = df[i - 1][j]
                else:
                    df[i][j] = min(df[i][j - coins[i - 1]] + 1, df[i - 1][j])


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