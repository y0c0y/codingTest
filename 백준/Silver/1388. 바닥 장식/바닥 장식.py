import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
totalCnt = 0
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        cntW = 0
        cntH = 0
        if board[i][j] == "-" and not visited[i][j]:
            for k in range(j + 1, m):
                if board[i][k] != "-":
                    cntW += 1
                    break
                else:
                    visited[i][k] = True
            if not cntW:  # 한 줄 끝까지 "-"인 경우
                cntW += 1
        elif board[i][j] == "|" and not visited[i][j]:
            for k in range(i + 1, n):
                if board[k][j] != "|":
                    cntH += 1
                    break
                else:
                    visited[k][j] = True
            if not cntH:  # 한 줄 끝까지 "|"인 경우
                cntH += 1
        # print(cntW, cntH)
        totalCnt += cntW + cntH
print(totalCnt)
