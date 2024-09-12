# Three Points for a Win    # 21022     # Bronze III

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

point = 0
for idx, score in enumerate(A):
    if score > B[idx]:     point += 3
    elif score == B[idx] : point += 1
    else:                  point += 0

print(point)