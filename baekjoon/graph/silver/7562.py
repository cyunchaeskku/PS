"""
SILVER I
"""
from collections import deque
from typing import List
import sys

input = sys.stdin.readline

t = int(input())

def solve():
    l = int(input())
    start_r, start_c = map(int, input().split())
    dst_r, dst_c = map(int, input().split())
    
    def bfs(l, start_r, start_c, dst_r, dst_c):
        visited = [[False] * l for _ in range(l)]
        q = deque([[start_r, start_c, 0]])
        visited[start_r][start_c] = True
        
        drs, dcs = [-1,-2, -2, -1, 1,2,2,1], [2,1,-1,-2,-2,-1,1,2]
        
        while q:
            r, c, distance = q.popleft()
            if r == dst_r and c == dst_c:
                return distance
            for dr , dc in zip(drs, dcs):
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < l and 0 <= nc < l and not visited[nr][nc]:
                    q.append([nr, nc, distance + 1])
                    visited[nr][nc] = True
        return 0
    
    ans = bfs(l, start_r, start_c, dst_r, dst_c)
    return ans

            
answer = []
for _ in range(t):
    answer.append(solve())
print("\n".join(map(str, answer)))