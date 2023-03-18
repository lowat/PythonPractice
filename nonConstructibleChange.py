def nonConstructibleChange(coins):
    currentMaxChange = 0
    coins.sort()
    for coin in coins:
        if(coin > currentMaxChange + 1):
            return currentMaxChange + 1
        currentMaxChange += coin
    return currentMaxChange + 1