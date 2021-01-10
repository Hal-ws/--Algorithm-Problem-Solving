import sys


def main():
    board =[]
    N, M, B = map(int, sys.stdin.readline().split())
    hCnt = [0] * 257
    maxH = -1
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    for i in range(N):
        for j in range(M):
            hCnt[board[i][j]] += 1
            if maxH <= board[i][j]:
                maxH = board[i][j]
    ansTime = 128000001
    ansH = -1
    for stdH in range(maxH, -1, -1):
        t, inven = 0, B
        flag = 1
        for h in range(256, -1, -1):
            cnt = hCnt[h] #각 h를 만족하는 길이의 수
            if stdH < h: #기준 높이보다 크다
                t += (h - stdH) * 2 * cnt # 시간 추가
                inven += (h - stdH) * cnt # inven에 더한다
            elif stdH > h: #기준 높이보다 낮다
                inven -= (stdH - h) * cnt
                if inven < 0:
                    flag = 0
                    break #인벤토리에 다 빔
                t += (stdH - h) * cnt # 시간 추가
        if flag: #배치 성공
            if t < ansTime:
                ansTime = t
                ansH = stdH
            if t == ansTime:
                if ansH < stdH:
                    ansH = stdH
    print('%s %s' %(ansTime, ansH))


if __name__ == '__main__':
    main()
