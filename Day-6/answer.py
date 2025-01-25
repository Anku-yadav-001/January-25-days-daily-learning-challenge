def cutRod(n, length, price):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = max(dp[i], price[j] + dp[i - length[j]])

    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    length = list(map(int, input().split()))
    price = list(map(int, input().split()))
    print(cutRod(n, length, price))