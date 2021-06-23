import sys


def main():
    while 1:
        tmpList = list(map(int, sys.stdin.readline().split()))
        if tmpList[0] == 0:
            break
        else:
            hList = tmpList[1:] + [0]
        stack = [[0, 0]] # 높이, 위치
        ans = 0
        for i in range(len(hList)):
            p, h = i + 1, hList[i]
            topH = stack[-1][0]
            if topH <= h:
                stack.append([h, p])
            else:
                tmpSize = 0
                while 1:
                    tmp = stack.pop()
                    tmpH, p2 = tmp[0], tmp[1]
                    if h >= tmpH:
                        stdH = lastH
                        stdP = p2
                        stack.append(tmp)
                        break
                    if tmpSize < tmpH * (p - p2):
                        tmpSize = tmpH * (p - p2)
                    lastH = tmpH
                if tmpSize < stdH * (p - stdP - 1):
                    tmpSize = stdH * (p - stdP - 1)
                stack.append([h, p])
                if ans < tmpSize:
                    ans = tmpSize
        print(ans)


if __name__ == '__main__':
    main()
