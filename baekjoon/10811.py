n, m = map(int, input().split())

baskets = [i+1 for i in range(n)]

def swap(i, j, baskets):
    temp = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = temp

for iter in range(m):
    i, j = map(int, input().split())
    # print("\n")
    if i == j:
        continue
    if j == i+1:
        swap(i,j,baskets)
    else:
        for inner_iter in range(i, int(j/2)+1):
            swap(i + inner_iter -1, j - inner_iter +1, baskets)
    # for ball in baskets:
        # print(ball, end=" ")
    # print("\n")
    
for ball in baskets:
    print(ball, end=" ")