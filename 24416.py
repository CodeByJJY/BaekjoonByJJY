# 알고리즘 수업 - 피보나치 수 1     # 24416


dp= [0 for _ in range(41)]

def fibonacci(n):
    dp[1], dp[2] = 1, 1

    for x in range(3, n+1):
        dp[x] = dp[x-1] + dp[x-2]

    return dp[n]
    

n = int(input())

print(fibonacci(n), n-2)