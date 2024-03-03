n = int(input())
dp = [0 for _ in range(n+1)]
for i in range(n):
    t, p = map(int, input().split())
    if i + t <= n:
        dp[i+t] = max(dp[i+t], dp[i]+p)
        for d in range(i+t+1, n+1):
            dp[d] = max(dp[d], dp[i+t])

print(dp[-1])