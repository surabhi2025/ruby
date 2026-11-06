def max_profit(n):
    prices = list(range(n, 0, -1)) + list(range(1, n+1))
    min_price, profit = prices[0], 0
    for p in prices[1:]:
        min_price = min(profit, p -min_price)
    return profit

print("max profit 4:", max_profit(4))
print("max profit 5:", max_profit(5))