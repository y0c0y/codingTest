import sys

sentence1 = sys.stdin.readline().strip() # 비교당한 문자열
sentence2 = sys.stdin.readline().strip() # 비교할 문자열

lenS1 = len(sentence1)
lenS2 = len(sentence2)

d = [0] * lenS2 # 문자 부분 수열 갯수를 저장할 리스트

for i in range(lenS1): # 문자열1의 문자를 하나씩 비교
    maxLen = 0 # 가장 긴 부분 수열의 길이를 저장할 변수
    for j in range(lenS2):
        if maxLen < d[j]: # 문자열1의 문자 이전의 문자열2의 문자들 중 가장 긴 부분 수열의 길이를 저장
            maxLen = d[j]
        elif sentence1[i] == sentence2[j]: # 문자열1의 문자와 문자열2의 문자가 같다면, 이전의 문자열2의 문자들 중 가장 긴 부분 수열의 길이에 +1
            d[j] = maxLen + 1
print(max(d)) # 가장 긴 부분 수열의 길이 출력