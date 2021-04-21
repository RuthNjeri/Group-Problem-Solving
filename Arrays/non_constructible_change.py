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