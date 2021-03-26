
def maximum_profit(prices):
    profit = 0
    for i, buy_price in enumerate(prices):
        print(buy_price)
        sell_price = max(prices[i:])
        print(sell_price)
        profit = max(profit, sell_price - buy_price)
        print(profit)
    return profit
eth_prices = [455, 460, 465, 451, 414, 415, 441]
print(maximum_profit(prices=eth_prices))
# ouput: 27