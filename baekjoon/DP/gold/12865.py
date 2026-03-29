"""
https://www.acmicpc.net/problem/12865
Gold V
"""

n, k = map(int, input().split())
w, v = [0] * (n+1), [0] * (n+1)

for i in range(1, n+1):
    a, b = map(int, input().split())
    w[i] = a
    v[i] = b
    
"""
1차원 배열
"""

# dp = [0] * (k+1)
# for i in range(1, n+1):
#     for weight in range(k, w[i] - 1, -1):
#         dp[weight] = max(dp[weight], dp[weight - w[i]] + v[i])
# print(dp[k])


"""
2차원 배열
"""
# dp[i][j] = 물건 i까지 고려했을 때, 무게 한도 j일 때 최대 가치
dp = [
    [0] * (k + 1) for _ in range(n+1)
]

for i in range(1, n+1):
    for weight in range(0, k+1):
        dp[i][weight] = dp[i-1][weight] # don't add stuff
        if weight >= w[i-1]: # if can add
            dp[i][weight] = max(dp[i][weight], dp[i-1][weight- w[i-1]] + v[i-1])
            
print(dp[n][k])