"""
SILVER II
"""
import sys
from typing import List
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = list()

start = None
for i in range(n):
    lis = list(input().rstrip())
    if 'I' in lis:
        start = [i,lis.index('I')]
    graph.append(lis)



def bfs(graph: List[List[str]]) -> int:
    ans = 0
    q = deque([start])
    drs, dcs = [0,1,0,-1],[1,0,-1,0]
    r, c = start
    graph[r][c] = 'X'
    
    while q:
        r, c = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] != 'X':
                q.append([nr, nc])
                if graph[nr][nc] == 'P':
                    ans += 1
                graph[nr][nc] = 'X'
                
    return ans

ans = bfs(graph)
if ans == 0:
    ans = 'TT'

print(ans)