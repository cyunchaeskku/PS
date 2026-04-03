"""
SILVER IV
"""
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

hash_map = {}

for card in cards:
    if card not in hash_map:
        hash_map[card] = 1
    else:
        hash_map[card] = hash_map[card] + 1
        
m = int(input())
target_cards = list(map(int, input().split()))

print(' '.join(str(hash_map.get(card, 0)) for card in target_cards))