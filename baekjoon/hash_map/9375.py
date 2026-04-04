"""
SILVER III
"""
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    clothes = {}
    for _ in range(n):
        item, category = input().split()
        
        if category not in clothes:
            clothes[category] = 1
        else:
            clothes[category] += 1
            
    total_combinations = 1
    for count in clothes.values():
        total_combinations *= (count + 1)
        
    return total_combinations - 1
    

t = int(input())
for _ in range(t):
    ans = solve()
    print(ans)