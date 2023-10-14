answer = []
len = 9
for i in range(len):
    n = int(input())
    answer.append(n)
maxNumber = max(answer)
index = answer.index(maxNumber)+1
print(maxNumber)
print(index)
