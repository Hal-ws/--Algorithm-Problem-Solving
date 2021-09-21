import sys


def main():
    while 1:
        hList = list(map(int, sys.stdin.readline().split()))
        if hList[0] == 0:
            break
        hList.append(0)
        stack = [[0, 0]] # 위치, 높이
        ans = 0
        for idx in range(1, len(hList)):
            curH = hList[idx]
            if stack[-1][1] <= curH:
                stack.append([idx, curH])
            else:
                lastH = None
                while 1:
                    tmp = stack.pop()
                    tIdx, tH = tmp[0], tmp[1]
                    w = idx - tIdx
                    if tH <= curH:
                        if ans <= (w - 1) * lastH:
                            ans = (w - 1) * lastH
                        stack.append([tIdx, tH])
                        stack.append([idx, curH])
                        break
                    if lastH != None:
                        if ans <= (w - 1) * lastH:
                            ans = (w - 1) * lastH
                    if ans <= w * tH:
                        ans = w * tH
                    lastH = tH
        print(ans)
    return


if __name__ == '__main__':
    main()
