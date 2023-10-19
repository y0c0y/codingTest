import sys

N = int(sys.stdin.readline())

cycle = []
check = -1

while True:
    if not len(cycle):
        cycle.append((N // 10, N % 10))
    check = cycle[-1][0] + cycle[-1][-1]
    # print(cycle)
    # print(check)
    if (cycle[-1][1] * 10 + check % 10) == N:
        print(len(cycle))
        break
    cycle.append((cycle[-1][1], check % 10))
    # print(cycle)
