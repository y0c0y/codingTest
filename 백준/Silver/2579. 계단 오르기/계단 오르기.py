import sys

n = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(n)]
stairs.insert(0, 0)
dp = [0 for _ in range(n + 1)]
dp[0] = stairs[0]
dp[1] = stairs[1]

for i in range(2, n + 1):
    dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])

print(dp[n])
