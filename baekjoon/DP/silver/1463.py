n = int(input())
dp = [float('inf')] * (n + 1)

# --- init ---
dp[1] = 0



# --- bottom-up ---
for i in range(2, n+1):
  dp[i] = dp[i-1] + 1 # always applicable
  
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i // 2] + 1)
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i // 3] + 1)  


print(dp[n])