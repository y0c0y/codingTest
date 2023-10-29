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

def knapsack(n, k, items):
    # DP 테이블 초기화
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # 아이템별로 반복
    for i in range(1, n + 1):
        # 현재 아이템의 무게와 가치
        weight, value = items[i-1]
        
        # 1부터 목표 무게(k)까지 반복
        for j in range(1, k + 1):
            # 현재 아이템의 무게가 현재 목표 무게보다 큰 경우 (배낭에 넣을 수 없는 경우)
            if j < weight:
                # 이전 아이템까지의 최대 가치 값을 가져옴
                dp[i][j] = dp[i - 1][j]
            else:  # 배낭에 현재 아이템을 넣을 수 있는 경우
                # 아이템을 넣지 않은 경우의 가치와, 아이템을 넣은 경우의 가치 중 큰 값을 선택
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
    
    # n개의 아이템과 k 무게를 가진 배낭의 최대 가치 반환
    return dp[n][k]

input = sys.stdin.readline
# 아이템의 수(n)와 배낭의 최대 무게(k) 입력
n, k = map(int, input().split())
# 아이템의 무게와 가치 입력
items = [list(map(int, input().split())) for _ in range(n)]
# 결과 출력
print(knapsack(n, k, items))
   

