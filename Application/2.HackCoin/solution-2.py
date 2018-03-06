import sys


def main(fiat_money, future_stock):

    actions = []
    hack_coin = 0
    for index, price in enumerate(future_stock[:-1]):

        # Купуваме
        if price < future_stock[index + 1]:
            if not hack_coin:
                hack_coin = fiat_money / price
                fiat_money = 0
                actions.append('buy')
                continue
            else:
                actions.append('hold')
                continue

        # Продаваме
        if price > future_stock[index + 1]:
            fiat_money, hack_coin, actions = sell_that_shit(price, hack_coin, actions, fiat_money)
            continue

        if price == future_stock[index + 1]:
            actions.append('hold')

    fiat_money, hack_coin, actions = sell_that_shit(future_stock[-1], hack_coin, actions, fiat_money)

    print("%.2f" % fiat_money, ', '.join(actions), sep="\n")


def sell_that_shit(price, hack_coins, action_list, real_money):
    if hack_coins:
        real_money = hack_coins * price
        hack_coins = 0
        action_list.append('sell')
    else:
        action_list.append('hold')
    return(real_money, hack_coins, action_list)


if __name__ == '__main__':
    fiat_money = int(sys.argv[1])
    future_stock = [int(price) for price in sys.argv[2].split(',')]
    main(fiat_money, future_stock)
