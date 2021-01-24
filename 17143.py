import sys


def main():
    global R, C, board, sharks
    R, C, M = map(int, sys.stdin.readline().split())
    board = [[[0, 0, 0, 0] for j in range(C)] for i in range(R)]
    sharks = []
    ans = 0
    for i in range(M):
        r, c, s, d, z = map(int, sys.stdin.readline().split())
        board[r - 1][c - 1] = [z, s, d, i]
        sharks.append([r - 1, c - 1, s, d, z])
    man = -1
    while man < C - 1:
        man += 1
        ans += getshark(man)
        for i in range(M):
            if sharks[i] != None: # 아직 안잡아먹힌 상어일때
                moving(i) #i 번 상어를 움직임
        for sIdx in range(M):
            s = sharks[sIdx]
            if s != None: # 아직 살아있는 상어일경우
                y, x, s, d, z = s[0], s[1], s[2], s[3], s[4]
                if board[y][x] == [0, 0, 0, 0]: #빈자리에 넣을경우
                    board[y][x] = [z, s, d, sIdx]
                else: #기존 상어가 있는자리에 넣을때
                    bIdx = board[y][x][3] # 이미 있던 상어 정보
                    if sharks[bIdx][4] < sharks[sIdx][4]: #집어넣는 상어가 더 클때
                        sharks[bIdx] = None # 기존 상어 삭제
                        board[y][x] = [z, s, d, sIdx]
                    else: #기존 상어가 더 클때
                        sharks[sIdx] = None # 새 상어 삭제
    print(ans)


def moving(sIdx):
    global R, C, board, sharks
    y, x, s, d, z = sharks[sIdx][0], sharks[sIdx][1], sharks[sIdx][2], sharks[sIdx][3], sharks[sIdx][4]
    board[y][x] = [0, 0, 0, 0] #움직였으니 지운다
    leftD = s
    if d == 1:
        nx = x
        if leftD <= y:
            ny = y - leftD
            sharks[sIdx] = [ny, nx, s, d, z]
        else: #한번 이상 꺾일때
            leftD = leftD - y
            turnSize = (leftD - 1) // (R - 1)
            if turnSize % 2 == 0: # 아래로 내려감
                ny = leftD - ((R - 1) * turnSize)
                sharks[sIdx] = [ny, nx, s, 2, z]
            else:
                ny = (R - 1) - (leftD - ((R - 1) * turnSize))
                sharks[sIdx] = [ny, nx, s, 1, z]
    if d == 2:
        nx = x
        if y + leftD <= R - 1: #방향전환 없음
            ny = y + leftD
            sharks[sIdx] = [ny, nx, s, d, z]
        else: #한번 이상 꺾일때
            leftD = leftD - (R - 1 - y)
            turnSize = (leftD - 1) // (R - 1)
            if turnSize % 2 == 0: #위로 올라감
                ny = (R - 1) - (leftD - ((R - 1) * turnSize))
                sharks[sIdx] = [ny, nx, s, 1, z]
            else: #아래로 내려감
                ny = leftD - ((R - 1) * turnSize)
                sharks[sIdx] = [ny, nx, s, 2, z]
    if d == 3:
        ny = y
        if x + leftD <= C - 1: #방향전환 없음
            nx = x + leftD
            sharks[sIdx] = [ny, nx, s, 3, z]
        else:
            leftD = leftD - (C - 1 - x) #맨 오른쪽 끝으로 이동
            turnSize = (leftD - 1) // (C - 1)
            if turnSize % 2 == 0: #왼쪽으로 감
                nx = (C - 1) - (leftD - ((C - 1) * turnSize))
                sharks[sIdx] = [ny, nx, s, 4, z]
            else: # 오른쪽으로 감
                nx = leftD - ((C - 1) * turnSize)
                sharks[sIdx] = [ny, nx, s, 3, z]
    if d == 4:
        ny = y
        if x - leftD >= 0:
            nx = x - leftD
            sharks[sIdx] = [ny, nx, s, d, z]
        else: #한번 이상 꺾일때
            leftD = leftD - x
            turnSize = (leftD - 1) // (C - 1)
            if turnSize % 2 == 0: # 오른족으로 감
                nx = leftD - ((C - 1) * turnSize)
                sharks[sIdx] = [ny, nx, s, 3, z]
            else:
                nx = (C - 1) - (leftD - ((C - 1) * turnSize))
                sharks[sIdx] = [ny, nx, s, 4, z]


def getshark(man):
    global R, C, board, sharks
    for i in range(R):
        if board[i][man] != [0, 0, 0, 0]:
            sIdx = board[i][man][3]
            size = board[i][man][0]
            sharks[sIdx] = None # 잡아먹혔으니 상어 리스트에서 지움
            board[i][man] = [0, 0, 0, 0] # 보드에도 지움
            return size
    return 0


if __name__ == '__main__':
    main()
