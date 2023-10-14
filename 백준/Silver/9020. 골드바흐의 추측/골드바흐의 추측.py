import math

def PrimeNumbers():
    cnt = 10000
    arr = [True for i in range(cnt+1)]  # 0,1을 제외한 모든 숫자가 소수(True)인 것으로 설정하고 시작한다.

    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(math.sqrt(cnt)) + 1):
        if arr[i] == True:  # i가 소수인 경우
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
        while i * j <= cnt:
            arr[i * j] = False
            j += 1
    return arr

T = int(input())
arr = PrimeNumbers()
for i in range(T):
    n = int(input())  # 2부터 1000까지 모든 수에 대하여 소수를 찾을 것이다.
    a1 = 0
    a2= 0
    minGap = float("inf")
    for j in range(n // 2,  1, -1):
        if arr[j] and arr[n-j]:
            gap = n-2*j
            if minGap > gap:
                minGap = gap
                a1 = j
                a2 = n-j
    print(a1, a2)