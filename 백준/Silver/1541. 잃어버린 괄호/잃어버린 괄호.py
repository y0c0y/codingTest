# 백준 1541번 문제 : 잃어버린 괄호
#  최초로 마이너스가 나오기 전까지 나오는 모든 숫자는 더할 수 밖에 없다.
# 이후 마이너스가 나오면 그 뒤에 나오는 모든 숫자는 빼주면 된다.

import sys

input = sys.stdin.readline

# 입력받기
arr = input().strip().split("-")  # -를 기준으로 문자열을 나눈다.
# print(arr)
s = 0
for i in arr[0].split("+"):  # 나눈 문자열을 +를 기준으로 나눈다.
    # print(arr[0])
    s += int(i)  # +를 기준으로 나눈 문자열을 모두 더한다.
for i in arr[1:]: # - 이후 부터 마지막까지
    # print(arr[1])
    for j in i.split("+"):
        s -= int(j)  # -를 기준으로 나눈 문자열을 모두 뺀다.
print(s)
