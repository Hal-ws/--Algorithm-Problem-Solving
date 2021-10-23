import sys


def main():
    mList = list(map(int, sys.stdin.readline().split()))
    board = [[0, 0, 0, [0, 0]] for i in range(33)]
    for i in range(21):
        board[i][2] = i * 2
        board[i][3][0] = i + 1 # 붉은색으로 감
        if i == 5:
            board[i][0] = 1
            board[i][3][1] = 21
        if i == 10:
            board[i][0] = 1
            board[i][3][1] = 25
        if i == 15:
            board[i][0] = 1
            board[i][3][1] = 27
    board[20][3] = [32, 0]
    board[21] = [0, 0, 13, [22, 0]]
    board[22] = [0, 0, 16, [23, 0]]
    board[23] = [0, 0, 19, [24, 0]]
    board[24] = [0, 0, 25, [30, 0]]
    board[25] = [0, 0, 22, [26, 0]]
    board[26] = [0, 0, 24, [24, 0]]
    board[27] = [0, 0, 28, [28, 0]]
    board[28] = [0, 0, 27, [29, 0]]
    board[29] = [0, 0, 26, [24, 0]]
    board[30] = [0, 0, 30, [31, 0]]
    board[31] = [0, 0, 35, [20, 0]]
    cases = []
    for i in range(1, 5):
        dfs([i], cases, 1)
    ans = 0
    for case in cases:
        ans = max(ans, getans(mList, board, case))
        for i in range(33):
            board[i][1] = 0   # 판 초기화
    print(ans)
    return 0

def getans(mList, board, case):
    horseInfo = [0, 0, 0, 0, 0]  # 1 ~ 4번 horse가 위치한 board의 index
    result = 0
    # 33개의 board. 판 종류 (빨강/파랑), 현재 위에 있는 말 종류, 점수, 다음 목적지
    for i in range(10): #i번째 턴
        mvCnt = mList[i]  #mvCnt만큼 이동
        hIdx = case[i]  # 이동하는 horse
        pos = horseInfo[hIdx]  # 현재 위치
        if pos == 32:  # 마지막에 도착한걸 움직일 의미 없음
            return 0
        color = board[pos][0]  # 현재 판의 색깔
        nxtPos = board[pos][3][color]  # 다음칸 위치
        for _ in range(mvCnt - 1):
            if nxtPos == 32:  # 도착함
                break
            nxtPos = board[nxtPos][3][0]
        if nxtPos != 32:  # 도착지가 아닐경우
            if board[nxtPos][1] != 0: #이미 판 위에 말이 있음. 실패
                return 0
            board[nxtPos][1] = hIdx
            result += board[nxtPos][2]
        horseInfo[hIdx] = nxtPos
        board[pos][1] = 0
    return result


def dfs(case, cases, cnt):
    if cnt == 10:
        cases.append(case[:])
    else:
        for i in range(1, 5):
            case.append(i)
            dfs(case, cases, cnt + 1)
            case.pop()


if __name__ == "__main__":
    main()
