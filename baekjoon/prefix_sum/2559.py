"""
SILVER III
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))

prefix_sum = [0] * (n+1)
for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + s[i]
answer = -float('inf')

for i in range(n-k+1):
    val = prefix_sum[i+k] - prefix_sum[i]
    answer = max(answer, val)
    
print(answer)