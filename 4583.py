# 거울상    # 4582

mirror = {'b':'d', 'd':'b', 'p':'q', 'q':'p', 'i':'i', 'o':'o', 'v':'v', 'w':'w', 'x':'x'}

while True:
    result = ''
    isResult = False
    text = input()

    if text == '#':
        break
    
    for alphabet in text[::-1]:
        if alphabet not in mirror:
            isResult = False
            print("INVALID")
            break
        else:
            isResult = True
            result += mirror[alphabet]
    
    if isResult:    print(result)