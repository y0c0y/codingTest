num_switch = int(input())  # 스위치 개수
state = input()
state = state.split()
state = [int(item) for item in state]
students = int(input())

for i in range(students):
    s, ns = map(int, input().split())
    if s == 1:  # 남자일때
        for j in range(1, num_switch + 1):
            if j % ns == 0:
                if state[j - 1]:
                    state[j - 1] = 0
                else:
                    state[j - 1] = 1
    else:  # 여자일때 (2)
        start = end = ns  # ns를 시작점 과 끝점으로
        j = 1
        while True:
            if ns - j >= 1 and ns + j <= num_switch:
                if state[ns - j - 1] == state[ns + j - 1]:
                    start = ns - j
                    end = ns + j
                else:
                    break
            else:
                break
            j += 1
        for j in range(start, end + 1):
            if state[j - 1]:
                state[j - 1] = 0
            else:
                state[j - 1] = 1

for i in range(len(state)):
    if i % 20 == 0 and i > 0:
        print()
    print(state[i], end=" ")
