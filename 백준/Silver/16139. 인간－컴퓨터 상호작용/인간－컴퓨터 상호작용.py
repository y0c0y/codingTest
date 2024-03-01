import sys

str = sys.stdin.readline().strip()
n = int(sys.stdin.readline())

for i in range(n):
    find, start, end = sys.stdin.readline().split(" ")
    start = int(start)
    end = int(end)
    tmp = str[start : end + 1]
    cnt = tmp.count(find)
    print(cnt)
