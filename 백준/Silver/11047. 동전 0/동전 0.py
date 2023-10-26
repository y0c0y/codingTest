n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))  # 오름차순으로 주어짐
coin.sort(reverse=True)  # 내림차순으로 정렬

count = 0 # 동전의 개수
for i in coin: # 큰 동전부터
    if k >= i: # k가 동전보다 크면
        count += k // i # 몫을 더해줌
        k %= i # 나머지를 k에 저장
print(count)