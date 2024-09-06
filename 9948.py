# Have you had your birthday yet?  # 9948  # Bronze II

while True:
    day, month = input().split()
    day = int(day)

    # 종료여부 확인하기
    if day == 0 and month == '#': break

    # 해당 케이스 여부 확인
    if month == 'August':
        if day == 4:    print("Happy birthday")
        elif day < 4:   print("Yes")
        else:           print("No")
    elif month == 'September' or month == 'October' or month == 'November' or month == 'December':
        print("No")
    else:
        if month == 'February' and day == 29:   print('Unlucky')
        else:                                   print('Yes')