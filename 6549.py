import sys


def main():
    while 1:
        tmpList = list(map(int, sys.stdin.readline().split()))
        if tmpList[0] == 0:
            break
        else:
            hList = tmpList[1:]
        stack = [[0, 0]] # 위치, 높이
        areaList = [[0, 0] for i in range(len(hList) + 1)]  # i번 bar로 끝나는 최대 직사각형의 가로 / 세로 길이 표시
        ans = 0
        for i in range(len(hList)):
            p, h = i + 1, hList[i]
            lastP, topH = stack[-1][0], stack[-1][1]
            print('i: %s' %i)
            if topH < h:
                thisW, thisH = areaList[lastP][0] + (p - lastP), areaList[lastP][1]
                if thisW * thisH <= h:
                    areaList[p][0] = 1
                    areaList[p][1] = h
                else:
                    areaList[p][0] = thisW + 1
                    areaList[p][1] = topH
            else: # 더 작거나 같은
                while len(stack) > 0:
                    if h <= stack[-1][1]:  # 현재 직사각형보다 더 작은것만 남겨둠
                        stack.pop()
                    else:
                        break
                lastP, lastH = stack[-1][0], stack[-1][1]

            stack.append([p, h])
            print('stack: %s' %stack)
            print('area: %s' %areaList)
            thisArea = areaList[i][0] * areaList[i][1]
            if ans < thisArea:
                ans = thisArea
        print(ans)


if __name__ == '__main__':
    main()
