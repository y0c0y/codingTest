import sys

# 재귀 깊이를 늘려줍니다 (주어진 입력 데이터의 크기를 고려하여)
sys.setrecursionlimit(10 ** 6)

# 숫자들을 저장할 리스트
num_list = []

# 입력을 계속 받아서 num_list에 저장합니다.
# EOF (End Of File)에 도달하면 입력 받기를 중단합니다.
while 1:
    try:
        num_list.append(int(sys.stdin.readline()))
    except:
        break

# 전위 순회 결과로부터 후위 순회 결과를 출력하는 함수
def postorder(first, end):
    # 재귀 종료 조건: 처리할 범위가 없을 때
    if first > end:
        return

    # 초기에 mid 값을 end + 1로 설정합니다.
    mid = end + 1

    # 주어진 범위 내에서 루트보다 큰 첫 번째 값(오른쪽 서브트리의 시작)을 찾아냅니다.
    for idx in range(first + 1, end + 1):
        if num_list[first] < num_list[idx]:
            mid = idx
            break

    # 왼쪽 서브트리에 대해 재귀 호출
    postorder(first + 1, mid - 1)

    # 오른쪽 서브트리에 대해 재귀 호출
    postorder(mid, end)

    # 후위 순회의 특징: 왼쪽 서브트리 -> 오른쪽 서브트리 -> 루트 순으로 처리
    # 따라서 루트 값을 출력합니다.
    print(num_list[first])

# 전체 범위에 대해 함수를 호출합니다.
postorder(0, len(num_list) - 1)
