# 수학은 체육과목입니다     # 17362     # Bronze IV

import sys

n = int(sys.stdin.readline().strip())

layer = (n-1)//4

if layer%2:
    print(5-(n-1)%4)
else:
    print((n-1)%4 + 1)