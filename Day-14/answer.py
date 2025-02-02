def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

t = int(input())
for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    print(max_profit(prices))