"""
skeleton code for
1. DFS
2. BFS
Baekjoon 1260 / SILVER II
"""


import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)


for i in range(1, m+1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n+1):
    graph[i].sort()
    

def dfs(node):
    global graph
    global visited
    
    visited[node] = True
    print(node, end=' ')
    
    for child in graph[node]:
        if not visited[child]:
            dfs(child)
            
dfs(v)
print()

def bfs(graph, start):
    visited = [False] * (n+1)
    q = deque([start])
    visited[start] = True
    
    while q:
        node = q.popleft()
        print(node, end= ' ')
        
        for child in graph[node]:
            if not visited[child]:
                q.append(child)
                visited[child] = True
                
bfs(graph, v)
print()