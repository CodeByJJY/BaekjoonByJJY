# 전화 요금     # 3226

N = int(input())
cnt = 0

for _ in range(N):
    HH_MM_DD = input()
    hour, min, dur = int(HH_MM_DD[0:2]), int(HH_MM_DD[3:5]), int(HH_MM_DD[6:])
    time = 60*hour + min

    for i in range(time+1, time + dur+1):
        if (7*60+1) <= i <= 60*19:   cnt += 10
        else:                       cnt += 5
    
print(cnt)