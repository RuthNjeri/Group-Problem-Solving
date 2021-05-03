class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        df = [[-1 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        df[0][0] = 0

        for i in range(1, len(df[0])):
            df[0][i] = float('inf')

        # coins.sort() # You may or may not need to sort
        self.dp(coins, amount, df)
        if df[len(coins)][amount] == float('inf'):
            return -1
        return df[len(coins)][amount]

    def dp(self, coins, amount, df):
        for i in range(1,len(coins)+1):
            df[i][0] = 0
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j < coins[i-1]:
                    df[i][j] = df[i-1][j]
                else:
                    df[i][j] = min(df[i][j-coins[i-1]] + 1, df[i-1][j])