import sys


def main():
    paperList = [0 for i in range(6)]
    answer = 0
    for i in range(6):
        paperList[i] = int(sys.stdin.readline())
    answer += paperList[5] # 6 * 6 사이즈일때
    if paperList[4] > 0: # 5 * 5 사이즈
        answer += paperList[4]
        leftSpace = 11  * paperList[4]
        paperList[0] -= leftSpace
        if paperList[0] < 0:
            paperList[0] = 0
    # 여기까진 ㄱㅊ
    if paperList[3] > 0: # 4 * 4 사이즈
        answer += paperList[3]
        leftSpace = 20 * paperList[3]
        if paperList[1] * 4 >= leftSpace: #leftspace 를 다 씀
            paperList[1] -= (leftSpace // 4)
        else: # 빈공간 남음
            leftSpace -= (paperList[1] * 4)
            paperList[1] = 0
            paperList[0] -= leftSpace
            if paperList[0] < 0:
                paperList[0] = 0
    if paperList[2] > 0: # 3 * 3 사이즈
        answer += (paperList[2] // 4)
        if paperList[2] % 4 != 0: # 정확하게 다 채울 수 없을 때
            answer += 1
            leftSpace = 36 - (9 * (paperList[2] % 4))
            if leftSpace == 9:
                if paperList[1] >= 1:
                    paperList[1] -= 1
                    leftSpace -= 4
            elif leftSpace == 18:
                if paperList[1] >= 3:
                    paperList[1] -= 3
                    leftSpace -= (4 * 3)
                else:
                    leftSpace -= (4 * paperList[1])
                    paperList[1] = 0
            elif leftSpace == 27:
                if paperList[1] >= 5:
                    paperList[1] -= 5
                    leftSpace -= (4 * 5)
                else:
                    leftSpace -= (4 * paperList[1])
                    paperList[1] = 0
            if leftSpace > 0 and paperList[0] > 0:
                if paperList[0] >= leftSpace:
                    paperList[0] -= leftSpace
                else:
                    paperList[0] = 0
    if paperList[1] > 0: # 2 * 2 사이즈
        answer += (paperList[1] // 9)
        if paperList[1] % 9 != 0: # 정확하게 다 채울수 없을때
            answer += 1
            leftSpace = 36 - (4 * (paperList[1] % 9))
            paperList[0] -= leftSpace
            if paperList[0] < 0:
                paperList[0] = 0
    if paperList[0] > 0: # 1 * 1 사이즈
        answer += (paperList[0] // 36)
        if paperList[0] % 36 != 0:
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()
