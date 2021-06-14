# https://leetcode.com/problems/coin-change/

# @param {Integer[]} coins
# @param {Integer} amount
# @return {Integer}

def coin_change(coins, amount)
    
  # dp[i][j] = min(dp[i][j - ci] + 1, dp[i - 1][j])
  # where i is the coins, j is the amount and ci is the current coin
  
  # Instead of creating a full table, we want to maintain two rows always. 
  
  dp = Array.new(coins.length + 1){Array.new(amount + 1)}
  
  for col in 0...dp[0].length
      dp[0][col] = Float::INFINITY
  end
  dp[0][0] = 0
  
  for i in 1..coins.length
      for j in 0...dp[0].length
          if j < coins[i - 1]
             dp[i][j] = dp[i - 1][j]
          else
             dp[i][j] = [dp[i][j - coins[i - 1]] + 1, dp[i - 1][j]].min
          end
      end
  end
  
  coins = dp[coins.length][amount]
  
  if coins == Float::INFINITY
    -1
  else
      coins
  end
  
end