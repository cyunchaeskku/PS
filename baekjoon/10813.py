n, m = map(int, input().split())

baskets = [i+1 for i in range(n)]
# print("size:", len(baskets))

for iter in range(m):
    i, j = map(int, input().split())
    temp = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = temp
        
for ball in baskets:
    print(ball, end=" ")