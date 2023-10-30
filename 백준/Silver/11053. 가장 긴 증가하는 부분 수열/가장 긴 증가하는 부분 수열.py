import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

d = [1 for _ in range(n)]  # 문자열2의 문자들 중 문자열1의 문자와 같은 문자들 중 가장 긴 부분 수열의 길이를 저장할 리스트

for i in range(1, n):  # 문자열1의 문자를 하나씩 비교
    for j in range(i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j] + 1)
print(max(d))  # 가장 긴 부분 수열의 길이 출력
