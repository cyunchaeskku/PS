"""
SILVER I
"""
import sys
input = sys.stdin.readline

INF = float('inf')
R, G, B = 0, 1, 2
answer = INF

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

dp = [[INF] * 3 for _ in range(n)]
for i in range(3):
    dp[0][i] = costs[0][i]
    
for i in range(1, n):
        dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + costs[i][R]
        dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + costs[i][G]
        dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + costs[i][B]
        
print(min(dp[n-1]))