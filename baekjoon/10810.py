n, m = map(int, input().split())

baskets = [0 for i in range(n)]
# print("size:", len(baskets))

for iter in range(m):
    i, j, k = map(int, input().split())
    for inner_iter in range(i, j+1):
        baskets[inner_iter -1] = k
        
for ball in baskets:
    print(ball, end=" ")