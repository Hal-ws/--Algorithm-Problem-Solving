import sys


def getans(num, p):
    direction = 1
    leftIdx = 0
    rightIdx = len(num) - 1
    ans = []
    for i in range(len(p) - 1):
        if p[i] == 'D':
            if leftIdx > rightIdx:
                print('error')
                return 0
            else:
                if direction > 0:
                    leftIdx += 1
                else:
                    rightIdx -= 1
        else:
            direction *= (-1)
    if leftIdx > rightIdx:
        print('[]')
        return 0
    if  direction > 0:
        print('[', end='')
        for i in range(rightIdx - leftIdx):
            print(num[leftIdx + i], end=',')
        print(str(num[rightIdx]) + str(']'))
    else:
        print('[', end='')
        for i in range(rightIdx - leftIdx):
            print(num[rightIdx - i], end=',')
        print(str(num[leftIdx]) + str(']'))

T = int(sys.stdin.readline())
for i in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    num = sys.stdin.readline()
    num = num[1:len(num) - 2]
    if len(num) > 0:
        num = list(map(int, num.split(',')))
    else:
        num = []
    getans(num, p)
