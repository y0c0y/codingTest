answer = []
N = int(input())

for i in range(N):
    tmp = int(input())
    answer.append(tmp)
answer.sort()
for i in answer:
    print(i)
