# 샤틀버스 #25625

x, y = map(int, input().split())

if y < x:
    print(x + y)
else:
    print(y - x)