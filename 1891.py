import sys


def main():
    d, num = map(int, sys.stdin.readline().split())
    dx, dy = map(int, sys.stdin.readline().split())
    num = str(num)
    luY, luX = 0, 0
    rdY, rdX = pow(2, d) - 1, pow(2, d) - 1
    for i in range(len(num)):
        midY = (luY + rdY) // 2
        midX = (luX + rdX) // 2
        if num[i] == '1':
            luX = midX + 1
            rdY = midY
        if num[i] == '2':
            rdY = midY
            rdX = midX
        if num[i] == '3':
            luY = midY + 1
            rdX = midX
        if num[i] == '4':
            luY = midY + 1
            luX = midX + 1
    y, x = luY - dy, luX + dx
    answer = ''
    if 0 <= y <= pow(2, d) - 1 and 0 <= x <= pow(2, d) - 1:
        luY, luX, rdY, rdX = 0, 0, pow(2, d) - 1, pow(2, d) - 1
        while 1:
            midY = (luY + rdY) // 2
            midX = (luX + rdX) // 2
            if y <= midY:
                if x <= midX:
                    answer += '2'
                    rdY = midY
                    rdX = midX
                else:
                    answer += '1'
                    luX = midX + 1
                    rdY = midY
            else:
                if x <= midX:
                    answer += '3'
                    luY = midY + 1
                    rdX = midX
                else:
                    answer += '4'
                    luY = midY + 1
                    luX = midX + 1
            if luY == rdY and luX == rdX:
                break
        print(answer)
    else:
        print(-1)


if __name__ == '__main__':
    main()
