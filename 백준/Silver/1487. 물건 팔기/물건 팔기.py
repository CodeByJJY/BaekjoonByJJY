# 물건 팔기     # 1487      # silver IV

amounts = []
delivery_fees = []
pricing_samples = []
results = []

# 사람 수
N = int(input())

# 최대 가능 금액, 배송비 추출
for _ in range(N):
    amount, delivery_fee = map(int, input().split())
    amounts.append(amount)
    delivery_fees.append(delivery_fee)

# 가격대 추출
pricing_samples.append(amounts[0])
for i in amounts:
    if i not in pricing_samples:
        pricing_samples.append(i)
pricing_samples.sort()

# 가격 설정 시 결과 모으기
for price in pricing_samples:
    sum = 0
    for i in range(N):
        if (amounts[i] >= price) and (price > delivery_fees[i]):
            sum += (price - delivery_fees[i])
    results.append(sum)

# 결과 출력
if max(results) <= 0:
    print(0)
else:
    max_profits = max(results)
    idx = results.index(max_profits)
    print(pricing_samples[idx])