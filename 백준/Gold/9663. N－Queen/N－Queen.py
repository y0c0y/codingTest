N = int(input())
cnt = 0
pos = [0] * N # 각 열에서 퀸의 위치를 출력
flag_a = [False]*N #각 행에 퀸을 배치했는지 체크
flag_b = [False]*(2*N-1) # (-1,+1)(+1,-1) 퀸 배치
flag_c = [False]*(2*N-1) # (-1,-1)(+1,+1) 퀸 배치


def put() -> None:
    for i in range(N):
        print(f'{pos[i]:2}', end=' ')
    print()

def set(i: int) -> None:
    global cnt
    for j in range(N):
        if not flag_a[j] and  not flag_b[i+j] and  not flag_c[i-j+N-1]: #j행에 퀸을 배치하지 않았으면
            pos[i] = j
            if i == N-1:# 모든 열에 퀸을 배치했다면
                cnt = cnt + 1
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+N-1] =True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+N-1] =False # 필요하지 않은 분기 없애기
set(0)
print(cnt)
