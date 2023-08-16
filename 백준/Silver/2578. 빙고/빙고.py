board = []
mc = []

for i in range(5):  # 철수의 보드판
    line = input()
    nums = line.split()
    board += [int(item) for item in nums]

for i in range(5):  # 철수의 보드판
    line = input()
    nums = line.split()
    mc += [int(item) for item in nums]

cnt = 0
gap = 5
for idx, num in enumerate(mc):
    board[board.index(num)] = 0
    for i in range(0, gap):
        if (
            board[i * gap] == 0
            and board[i * gap + 1] == 0
            and board[i * gap + 2] == 0
            and board[i * gap + 3] == 0
            and board[i * gap + 4] == 0
        ):
            cnt += 1
        if (
            board[i] == 0
            and board[i + gap] == 0
            and board[i + gap * 2] == 0
            and board[i + gap * 3] == 0
            and board[i + gap * 4] == 0
        ):
            cnt += 1
    if (
        board[0] == 0
        and board[6] == 0
        and board[12] == 0
        and board[18] == 0
        and board[24] == 0
    ):
        cnt += 1
    if (
        board[4] == 0
        and board[8] == 0
        and board[12] == 0
        and board[16] == 0
        and board[20] == 0
    ):
        cnt += 1
    if cnt >= 3:
        print(idx + 1)
        break
    else:
        cnt = 0

