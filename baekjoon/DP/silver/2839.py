import sys

''' https://www.acmicpc.net/problem/2839 '''
'''
3키로그램, 5키로그램 봉지가 있다.
N킬로그램 배달해야 할 때 필요한 봉지의 최소 개수 구하고 싶다.
전형적인 DP 문제
3 <= N <= 5_000
'''
MAX_N = 5_000
n = int(input().strip())

# dp[i]: i 키로그램 배달할 때 최소의 봉지 개수
dp = [float('inf')] * (MAX_N+1)

# --- init ---
dp[0] = 0
dp[3] = 1
dp[5] = 1


# --- bottom up ---
for i in range(6, n+1):
  for kilo in [3, 5]:
    dp[i] = min(dp[i], dp[i - kilo] + 1)
    

# --- answer ---
ans = dp[n] if dp[n] != float('inf') else -1
print(ans)

"""
[최적해]
3부터 i가 순회하면 자동으로 초기화하므로 init 단계가 필요 없다
---
import sys

MAX_N = 5_000
n = int(input().strip())

dp = [float('inf')] * (MAX_N + 1)
dp[0] = 0

for i in range(3, n + 1):
    for kilo in [3, 5]:
        if i - kilo >= 0 and dp[i - kilo] != float('inf'):
            dp[i] = min(dp[i], dp[i - kilo] + 1)

ans = dp[n] if dp[n] != float('inf') else -1
print(ans)
"""
