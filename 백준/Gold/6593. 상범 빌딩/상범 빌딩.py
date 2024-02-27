# bfs

import sys
from collections import deque

visited = []
building = []

dx = [1, -1, 0, 0, 0, 0]  # 동,서,남,북,상,하
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

l, c, r = 0, 0, 0


def resetAll(l, c, r):
    global visited, building
    visited = [[[0] * r for _ in range(c)] for _ in range(l)]
    building = []


def isIndex(X, Y, Z):
    global l, c, r

    if not (0 <= X < r):
        return False
    if not (0 <= Y < c):
        return False
    if not (0 <= Z < l):
        return False
    return True


def canMove(X, Y, Z):
    global visited
    check = building[Z][Y][X]
    if check == ".":  # can move
        return 1
    elif check == "E":  # escape
        return 2
    else:
        return 0
    # if check == "S":  # loop
    #     return 3


def bfs(x, y, z):
    global visited, building

    q = deque(())
    q.append((x, y, z))
    visited[z][y][x] = 1

    while q:
        tmp = q.popleft()
        for i in range(6):
            X = tmp[0] + dx[i]
            Y = tmp[1] + dy[i]
            Z = tmp[2] + dz[i]
            if isIndex(X, Y, Z) and visited[Z][Y][X] == 0:
                check = canMove(X, Y, Z)
                if check == 1:
                    visited[Z][Y][X] = visited[tmp[2]][tmp[1]][tmp[0]] + 1
                    q.append((X, Y, Z))
                    # print(Z, Y, X, visited[Z][Y][X])
                elif check == 2:
                    return visited[tmp[2]][tmp[1]][tmp[0]]

    return 0


while True:
    l, c, r = map(int, sys.stdin.readline().split(" "))

    if not (l or c or r):
        break

    resetAll(l, c, r)

    startX, startY, startZ = 0, 0, 0

    for i in range(l):  # floor
        tmps = []
        for j in range(c):  # column
            tmp = list(sys.stdin.readline())
            tmp.pop()
            if "S" in tmp:
                startZ = i
                startY = j
                startX = tmp.index("S")
            tmps.append(tmp)
        building.append(tmps)
        tmp = sys.stdin.readline()  # blank line each floor

    result = bfs(startX, startY, startZ)

    if not result:
        print("Trapped!")
    else:
        print(f"Escaped in {result} minute(s).")
