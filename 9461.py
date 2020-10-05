import sys
T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())

    if(N <= 5):
        if(N <= 3):
            ans = 1
        elif(N <= 5):
            ans = 2
    first = 1
    second = 1
    third = 1
    forth = 2
    fifth = 2
    for i in range(N - 5):
        ans = first + fifth
        first = second
        second = third
        third = forth
        forth = fifth
        fifth = ans
    print(ans)
