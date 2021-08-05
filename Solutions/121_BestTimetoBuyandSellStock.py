def BestTimetoBuyandSellStock(prices):

    max_margin = 0
    min_price = prices[0]

    if len(prices) < 2:
        return max_margin

    for price in prices:
        min_price = min(min_price,price)
        max_margin = max(max_margin, price - min_price)

    return max_margin


print(BestTimetoBuyandSellStock([1,1,5,3,0]))