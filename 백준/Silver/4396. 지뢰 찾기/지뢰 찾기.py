n = int(input())
map = []  # 지뢰 표시
user = []  # 오픈된 보드판
board = []  # 출력
check = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
    [-1, -1],
    [-1, 1],
    [1, -1],
    [1, 1],
]  # 상, 하, 좌, 우, 상좌, 상우, 하좌, 하우

# 지뢰
for i in range(n):
    line = input()
    map.append(list(line))

# 오픈된 보드판
for i in range(n):
    line = input()
    user.append(list(line))

flag = 0
# 출력할 보드판 초기화
for i in range(n):
    line = ""
    for j in range(n):
        line += "."
    board.append(list(line))

    # 출력
for y, line in enumerate(user):
    for x, ch in enumerate(line):
        if ch == "x":
            if map[y][x] == ".":
                cnt = 0
                # 폭탄 있는지 검사
                for item in check:
                    pre_y = y + item[0]
                    pre_x = x + item[1]
                    if (pre_y >= 0 and pre_y < n) and (pre_x >= 0 and pre_x < n):
                        if map[pre_y][pre_x] == "*":
                            cnt += 1
                    board[y][x] = str(cnt)
            else:
                flag = 1

if flag:
    for y, line in enumerate(map):
        for x, ch in enumerate(line):
            if ch == "*":
                board[y][x] = "*"

for line in board:
    new_line = "".join(line)
    print(new_line)
