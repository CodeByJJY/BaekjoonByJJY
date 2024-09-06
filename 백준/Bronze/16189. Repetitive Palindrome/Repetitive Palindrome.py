# Repetitive Palindrome     # 16189

s = input()
k = int(input())

if (s == "".join(list(reversed(s)))):
    print("YES")
else:
    print("NO")