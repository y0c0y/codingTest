# 백준 9084번 문제 - 동전

"""
알고리즘 요약:

1. M+1 크기의 배열 dp를 모두 0으로 초기화합니다. dp[0] = 1로 설정합니다. 
왜냐하면 0원을 만드는 방법은 하나뿐이기 때문입니다 (어떠한 동전도 사용하지 않음).

2. 각 동전에 대해, 해당 동전의 금액부터 M까지의 금액을 순회합니다. 
각 금액에 대해, 해당 금액에서 동전의 금액을 뺀 금액을 만드는 방법의 수를 더합니다. 
이는 현재 동전을 사용하여 금액을 만드는 방법을 효과적으로 계산합니다.

3. 모든 동전을 고려한 후, dp[M]은 금액 M을 만드는 전체 방법의 수를 제공할 것입니다.
"""

import sys

T = int(sys.stdin.readline())   # 테스트 케이스 개수
for _ in range(T):
    N = int(sys.stdin.readline())   # 동전의 가지 수
    coins = list(map(int, sys.stdin.readline().split()))    # 동전의 가치
    M = int(sys.stdin.readline())   # 만들어야 할 금액
    dp = [0] * (M + 1)   # dp[i] = 금액 i를 만들 수 있는 경우의 수
    dp[0] = 1
    for coin in coins:
        for i in range(coin, M + 1):
            dp[i] += dp[i - coin]
    print(dp[M])