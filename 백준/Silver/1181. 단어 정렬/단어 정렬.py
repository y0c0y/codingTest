answer = []
N = int(input())

for i in range(N):
    tmp = input()
    answer.append(tmp)
answer = set(answer)
answer = sorted(answer, key=lambda x: (len(x), x))
for i in answer:
    print(i)
