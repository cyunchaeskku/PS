from collections import deque
import sys

input = sys.stdin.readline

v = int(input()) # v: vertex. num of vertex
e = int(input()) # e: edge. num of edges

graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)
ans = 0

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(node, visited):
    global ans
    visited[node] = True
    # print(node, end=' ')
    ans += 1
    
    for child in graph[node]:
        if not visited[child]:
            dfs(child, visited)
        
def bfs(graph, start, v):
    global ans
    visited = [False] * (v+1)
    q = deque([start])
    visited[start] = True
    
    while q:
        node = q.popleft()
        ans += 1
        print(node, end=' ')
        
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                q.append(child)
    

# dfs(1, visited)
bfs(graph, 1, v)
print()
print(ans-1)