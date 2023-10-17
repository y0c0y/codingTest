import sys

sys.setrecursionlimit(100000)


def multiply(n):
    if n == 1:
        return A % C
    tmp = multiply(n // 2)
    if n % 2 == 1:
        return ((tmp * tmp) * A) % C
    else:
        return (tmp * tmp) % C


A, B, C = map(int, sys.stdin.readline().split())
print(multiply(B))
