def number_of_paths(n):
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[0][i] = 1

    for i in range(1, n):
        for j in range(n):
            if j >= i:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]
