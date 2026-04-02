"""
https://www.acmicpc.net/problem/10942
GOLD IV
"""

import sys

n = int(input())
nums = [0] + list(map(int, input().split()))

dp = [[False] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = True
    
for i in range(1, n):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = True
        

for length in range(3, n+1):
    for i in range(1, n - length + 2):
        if nums[i] == nums[i + length-1] and dp[i+1][i + length - 2]:
                dp[i][i + length-1] = True


m = int(input())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(int(dp[s][e]))