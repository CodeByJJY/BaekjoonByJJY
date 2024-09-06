# Amusement Park Adventure  # 29986

N, H = map(int, input().split())
limits = list(map(int, input().split()))
cnt = 0

for num in limits:
    if H >= num:    cnt += 1

print(cnt)