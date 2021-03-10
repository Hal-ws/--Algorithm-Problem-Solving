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
                while h < stack[-1][0]:
                    tmp = stack.pop()
                    tmpH, p2 = tmp[0], tmp[1]
                    if tmpSize < tmpH * (p - p2):
                        tmpSize = tmpH * (p - p2)
                firstP = stack[-1][1]
                if tmpSize < (p - firstP) * h:
                    tmpSize = (p - firstP) * h
                stack.append([h, p])
                if ans < tmpSize:
                    ans = tmpSize
        print(ans)


if __name__ == '__main__':
    main()
