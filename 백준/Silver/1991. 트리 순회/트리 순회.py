import sys

N = int(sys.stdin.readline())
root = [list(sys.stdin.readline().split()) for _ in range(N)]

def pre(n):
    if n > N:
        return
    print(root[n][0], end="")
    if root[n][1] != ".":
        tmp = [c[0] for c in root].index(root[n][1])
        pre(tmp)
    if root[n][2] != ".":
        tmp = [c[0] for c in root].index(root[n][2])
        pre(tmp)

def mid(n):
    if n > N:
        return
    if root[n][1] != ".":
        tmp = [c[0] for c in root].index(root[n][1])
        mid(tmp)
    print(root[n][0], end="")
    if root[n][2] != ".":
        tmp = [c[0] for c in root].index(root[n][2])
        mid(tmp)

def last(n):
    if n > N:
        return
    if root[n][1] != ".":
        tmp = [c[0] for c in root].index(root[n][1])
        last(tmp)
    if root[n][2] != ".":
        tmp = [c[0] for c in root].index(root[n][2])
        last(tmp)
    print(root[n][0], end="")


pre(0)
print()
mid(0)
print()
last(0)
