def checkio(price, denominations):
    coins_needed = [0 for _ in range(min(denominations))]
    for money in range(min(denominations), price+1):
        min_coins = money
        for coin in [d for d in denominations if d <= money]:
            if coins_needed[money-coin] == 0 and money not in denominations:
                min_coins = 0
                break
            else:
                min_coins = min(min_coins, coins_needed[money-coin] + 1)
        coins_needed.append(min_coins)
    return coins_needed[-1] if coins_needed[-1] else None


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(8, [1, 3, 5]) == 2
    assert checkio(12, [1, 4, 5]) == 3
    print('Done')
