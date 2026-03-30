"""
https://www.acmicpc.net/problem/2294
GOLD V
"""

n, k = map(int, input().split())
dp = [float('inf')] * (k+1)
dp[0] = 0
coins = []

for i in range(n):
    coins.append(int(input()))
    
for value in range(1, k+1):
    for coin in coins:
        if value - coin >= 0:
            dp[value] = min(dp[value], dp[value-coin]+1)

ans = dp[k] if dp[k] != float('inf') else -1
print(ans)