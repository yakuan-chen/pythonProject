def minNumberOfCoinsForChange(n, denoms):
    numofCoins = [float("Inf") for amount in range(n + 1)]
    numofCoins[0] = 0
    for denom in denoms:
        for amount in range(len(numofCoins)):
            if denom <= amount:
                numofCoins[amount] = min(numofCoins[amount], 1 + numofCoins[amount - denom])
    return numofCoins[n] if numofCoins[n] != float("Inf") else -1