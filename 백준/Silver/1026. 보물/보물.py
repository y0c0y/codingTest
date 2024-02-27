import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split(" ")))
b = list(map(int, sys.stdin.readline().split(" ")))

a.sort()

# print(a, b)

s = 0

for i in range(n):
    tmp = max(b)
    tmpIdx = b.index(tmp)
    tmpB = b.pop(tmpIdx)
    tmpA = a.pop(0)
    s += tmpA * tmpB
print(s)
