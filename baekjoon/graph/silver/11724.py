"""
SILVER II
"""
from collections import deque
import sys
from typing import List

input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

def bfs(graph: List[List[int]], visited: List[bool], start: int) -> None:
    q = deque([start])
    visited[start] = True
    
    while q:
        node = q.popleft()
        
        for child in graph[node]:
            if not visited[child]:
                q.append(child)
                visited[child] = True
                
ans = 0
for i in range(1, n+1):
    if not visited[i]:
        ans += 1
        bfs(graph, visited, i)
        
print(ans)