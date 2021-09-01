import sys


def main():
    while 1:
        tmpList = list(map(int, sys.stdin.readline().split()))
        if tmpList[0] == 0:
            break
        else:
            hList = tmpList[1:]
        stack = [[0, 0]] # 높이, 위치
        ans = 0
        for i in range(len(hList)):
            p, h = i + 1, hList[i]
            topH = stack[-1][0]
            print('stack: %s' %stack)
            if topH < h:
                if topH == 0:
                    if ans < h:
                        ans = h
                elif ans < topH * (p - stack[-1][1] + 1):
                    ans = topH * (p - stack[-1][1] + 1)
            else:
                tmpSize = 0
                while len(stack) > 0:
                    if stack[-1][0] < h:
                        tmpSize = h * (p - stack[-1][1])
                        break
                    else:
                        stack.pop()
                if ans < tmpSize:
                    ans = tmpSize
            stack.append([h, p])
            print('answer: %s' %ans)
        print(ans)


if __name__ == '__main__':
    main()
