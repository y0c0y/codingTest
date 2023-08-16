jun_money = sung_money = int(input(""))  # 준현이와 성민이에게 주어진 현금
jun_stock = sung_stock = 0

prices = input()  # 주가 리스트(공백)
list = prices.split(" ")  # 공백을 기준으로 쪼개기
# 문자열 리스트를 정수 리스트로 변환하기
prices_list = [int(item) for item in list]

# 준현이 BNS
for price in prices_list:
    if jun_money >= price:
        stock = jun_money // price
        jun_stock += stock
        jun_money -= stock * price

# 성민이  TIMING
for day in range(len(prices_list)):
    if day >= 3:
        # 3일 연속 상승
        if (
            prices_list[day - 3]
            < prices_list[day - 2]
            < prices_list[day - 1]
            < prices_list[day]
        ):
            # 전량 매도
            sung_money += sung_stock * prices_list[day]
            sung_stock = 0
        # 3일 연속 하락
        if (
            prices_list[day - 3]
            > prices_list[day - 2]
            > prices_list[day - 1]
            > prices_list[day]
        ) and sung_money >= prices_list[day]:
            # 전량 매수
            stock = sung_money // prices_list[day]
            sung_stock += stock
            sung_money -= stock * prices_list[day]

jun_total = jun_money + prices_list[-1] * jun_stock  # 준현이 총액

sung_total = sung_money + prices_list[-1] * sung_stock  # 성민이 총액


if jun_total > sung_total:
    print("BNP")
elif jun_total < sung_total:
    print("TIMING")
else:
    print("SAMESAME")
