S = int(input())

if S <= 2:
    print(1)
else:
    n = 2
    endFlag = 0
    while True:
        if S < (n * (n + 1)) // 2:
            n -= 1
            endFlag = 1
            break
        elif S == (n * (n + 1)) // 2:
            endFlag = 1
            break
        if endFlag == 0:
            n += 1
    print(n)
