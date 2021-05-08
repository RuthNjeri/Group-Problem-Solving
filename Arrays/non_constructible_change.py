# The idea is that if you order the coins,
# you will always get the minimum number of possible
# coins you can create as you add them up
# if the next coin is larger than the current_sum + 1
# then the coin you cannot create is the current_sum + 1
# Example, with [1, 2, 4]
# You can creat 1, 2, 3, 4, 5, 6, 7 because the total so far is 7 and at each point
# the coin was not greater than the total + 1
# total = 0 current_coin = 1, current_coin > total + 1 = false
# total = 1 current_coin = 2, current_coin > total + 1 = false
# total = 3 current_coin = 4, current_coin > total + 1 = false
# return total + 1 which is 8, you cannot create 8 from 4, 2, and 1 

def nonConstructibleChange(coins):
  coins.sort()
  currentChangeCreated = 0

  for coin in coins:
    if coin > currentChangeCreated + 1:
      return currentChangeCreated + 1

    currentChangeCreated += coin


  return currentChangeCreated + 1

# Test Cases
nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]) # 20
nonConstructibleChange([1, 2, 5]) # 4
nonConstructibleChange([5, 8, 20]) # 1