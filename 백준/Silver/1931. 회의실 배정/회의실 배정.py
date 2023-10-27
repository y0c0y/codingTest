import sys

n = int(sys.stdin.readline())  # 회의의 수
time = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 회의 시간을 담을 리스트

time.sort(
    key=lambda x: (x[1], x[0])
)  # 끝나는 시간을 기준으로 오름차순 정렬, 끝나는 시간이 같다면 시작 시간을 기준으로 오름차순 정렬

cnt = 0  # 회의의 최대 개수
end_time = 0  # 회의가 끝나는 시간
for i in range(n):
    if time[i][0] >= end_time:  # 시작 시간이 끝나는 시간보다 크거나 같다면
        cnt += 1  # 회의 개수 증가
        end_time = time[i][1]  # 끝나는 시간 갱신
print(cnt)
