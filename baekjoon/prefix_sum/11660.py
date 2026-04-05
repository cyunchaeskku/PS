"""
SILVER I
still in progress
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    
prefix_sum = [[0] * n for _ in range(n)]
prefix_sum[0][0] = arr[0][0]

for r in range(n):
    for c in range(n-1):
        if c == 0 and r > 0:
            prefix_sum[r][c] = prefix_sum[r-1][n-1] + arr[r][c]
        prefix_sum[r][c+1] = prefix_sum[r][c] + arr[r][c+1]
        
# for pre in prefix_sum:
#     print(pre)

ans = []
for _ in range(m):
    sum_ = 0
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    
    sum_ = (prefix_sum[r2][c2] - prefix_sum[r1][c1]) if (r1 != r2 or c1 != c2) else arr[r1][c1]
            
    ans.append(sum_)
    
print("\n".join(map(str, ans)))