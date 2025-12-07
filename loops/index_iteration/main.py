prices = [29.99, 45.50, 12.75, 38.20]



for cost in range(len(prices)):
    if cost == 0:
        factor = 0.9
    elif cost == 1:
        factor = 0.8
    elif cost == 2:
        factor = 0.85
    elif cost == 3:
        factor = 0.95
    updated_price = prices[cost] * factor
    prices[cost] = updated_price
    print (f"Updated price for item {cost+1}: ${updated_price:.2f}")
