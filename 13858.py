# Reading Digits    # 13858     # Bronze I

def encoding(code):
    result = ""
    cnt = 1
    tmp = code[0]

    for i in code[1:len(code)-1]:
        if tmp != i:
            result += str(cnt)
            result += tmp
            tmp = i
            cnt = 1
        else:
            cnt += 1

    if tmp == code[-1]:
        cnt += 1
        result += str(cnt)
        result += tmp
    else:
        result += str(cnt)
        result += tmp
    
    return result



k, pos = map(int, input().split())
s = input()

for _ in range(k):
    s = encoding(s)

print(s[pos-1])