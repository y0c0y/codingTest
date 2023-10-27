import sys

sentence1 = sys.stdin.readline().strip()
sentence2 = sys.stdin.readline().strip()

lenS1 = len(sentence1)
lenS2 = len(sentence2)

d = [0] * lenS2

for i in range(lenS1):
    maxLen = 0
    for j in range(lenS2):
        if maxLen < d[j]:
            maxLen = d[j]
        elif sentence1[i] == sentence2[j]:
            d[j] = maxLen + 1
print(max(d))