# '1' : 첫번째 기둥
# '2' : 두번째 기둥
# '3' : 세번째 기둥
def hanoi(N, start, to, via):
    if N == 0:
        return
    hanoi(N - 1, start, via, to)
    print(start, to)
    hanoi(N - 1, via, to, start)

N = int(input())
print(2 ** (N) - 1)
if N <= 20:
    hanoi(N, "1", "3", "2")
