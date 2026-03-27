import sys
from collections import deque

n = int(input())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

size_shark = 2
r_shark, c_shark = 0,0

for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            r_shark, c_shark = i, j

drs, dcs = [0,-1,0,1],[1,0,-1,0]
def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# def calculate_distance(r1, c1, r2, c2):



# 먹을 수 있는 크기의 물고기의 list를 반환한다.
def find_fish():
    global size_shark

    fishes = []
    for r in range(n):
        for c in range(n):
            if a[r][c] != 9 and 0 < a[r][c] < size_shark:
                fishes.append((r, c))
    return fishes

# 상어가 r,c에서 x,y 좌표로 이동을 시도한다. (자기보다 큰 물고기에 막힐 수도 있음)
def move(r, c, x, y):
    global drs, dcs, size_shark, elapsed_time

    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((r, c))
    visited[r][c] = 0

    while q:
        r, c = q.popleft()
        if r == x and c == y:
            a[r][c] = 0
            elapsed_time += visited[r][c]
            return True
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if in_range(nr, nc) and size_shark >= a[nr][nc] and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

    return False



elapsed_time = 0
while True:
    fishes = find_fish()
    
    # fishes 리스트에는 먹을 수 있는 물고기의 좌표들이 들어있다. 이걸 기준대로 정렬하여, 항상 fishes[0]만 먹으러 갈 수 있도록.
    fishes.sort(key=lambda x : [x[0],x[1]])
    if len(fishes) == 0:
        break
    tx, ty = fishes[0]
    if move(r_shark, c_shark, tx, ty) == False:
        break

print(elapsed_time)