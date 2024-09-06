# The candy war     # 9038      # silver V

# 본인이 가진 캔디를 분배
def game(candies):
    tmp = candies.copy()

    for i in range(1, len(candies)):
        candies[i] //= 2
        candies[i] += tmp[i-1] // 2
    
    candies[0] //= 2
    candies[0] += tmp[-1] // 2

    return candies

# 홀수인지 확인하고, 홀수면 +1을 해서 반환
def is_odd(candies):
    for i in range(len(candies)):
        if candies[i]%2:
            candies[i] += 1
    return candies

# 모두 동일한 캔디를 가졌는지 여부 확인
def is_same(candies):
    result = True
    for i in range(1, len(candies)):
        if candies[0] != candies[i]:
            result = False
            break
    return result

T = int(input())

for _ in range(T):
    cnt = 0
    N = int(input())
    childs = list(map(int, input().split()))
    childs = is_odd(childs)

    while True:
        if is_same(childs):
            print(cnt)
            break

        childs = game(childs)
        childs = is_odd(childs)
        cnt += 1