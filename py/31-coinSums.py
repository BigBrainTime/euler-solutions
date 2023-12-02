#In Progress
valid_coins = (1,2,5,10,20,50,100,200)

coins = {}

def split(coin):
    divcoins = 1
    for divcoin in reversed(valid_coins[:valid_coins.index(coin)]):
        if divcoin < coin:
            divcoins += coins[divcoin]
            coin -= coin//divcoin
    return divcoins

for coin in valid_coins:
    if coin in (1,2):
        coins[coin]=coin

    else:
        coins[coin]=split(coin)

print(coins)