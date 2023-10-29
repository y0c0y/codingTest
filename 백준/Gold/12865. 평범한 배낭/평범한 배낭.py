# 백준 12865번 문제 - 평범한 배낭

"""
냅색 알고리즘 -  배낭 문제
배낭에 담을 수 있는 무게의 최댓값이 정해져 있고, 
일정한 가치의 무게가 정해진 짐들을 배낭에 담을 때, 
가치의 합이 최대가 되는 조합을 찾는 알고리즘

- Fractional Knapsack Problem
물건을 쪼갤 수 있는 배낭 문제로, 가치가 높은 순으로 정렬한 뒤 배낭에 담고,
텍스트남은 부분은 물건을 쪼개어 넣어 조합을 찾을 수 있음. 
그리디 알고리즘으로 해결 가능

Knapsack Problem
물건을 쪼갤 수 없는 배낭 문제로, 
동적계획법(Dynamic Programming)을 활용해 해결 가능
"""


# dp[i][j] = i번째 물건까지 고려했을 때, j 무게까지 담을 수 있는 최대 가치
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst=[[0, 0]]
for _ in range(n):
    lst.append(list(map(int, input().split())))
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        weight = lst[i][0]
        value = lst[i][1]
        if j < weight:  # 가방에 넣을 수 없으면
            dp[i][j] = dp[i - 1][j]  # 위에 값 그대로 가져오기
        else: # 가방에 넣을 수 있으면
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
print(dp[n][k])


