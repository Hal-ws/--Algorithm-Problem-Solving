import sys


def main():
    R, C = map(int, sys.stdin.readline().split())
    board = []
    cBoard = [[[] for j in range(C)] for i in range(R)] # crazy arduino들이 잇음
    dy = [1, 1, 1, 0, 0, 0, -1, -1, -1]
    dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    crazy = []
    for _ in range(R):
        board.append(list(sys.stdin.readline()[:C]))
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'I':
                jongsu = [i, j] #
            if board[i][j] == 'R':
                crazy.append([i, j])
                board[i][j] = len(crazy) - 1 # 미친 아두이노의 idx를 정해줌
    mvList = list(sys.stdin.readline())
    for i in range(len(mvList)):
        if i == len(mvList) - 1:
            mvList.pop()
        else:
            mvList[i] = int(mvList[i]) - 1
    for i in range(len(mvList)):
        d = mvList[i]
        y, x = jongsu[0], jongsu[1]
        ny, nx = y + dy[d], x + dx[d]
        if board[ny][nx] != 'I' and board[ny][nx] != '.': # 미친 아두이노를 만남
            print('kraj %s' %(i + 1))
            return
        else:
            board[ny][nx] = 'I' # 종수의 아두이노를 ny, nx 로 이동
            if d != 4:
                board[y][x] = '.'
            jongsu = [ny, nx]
            for cIdx in range(len(crazy)): # 미친 아두이노들 이동 시작
                if crazy[cIdx] != None: # 폭파된 아두이노가 아니면 이동
                    ay, ax = crazy[cIdx][0], crazy[cIdx][1]
                    minDis = 201
                    minIdx = None
                    for j in range(9):
                        nay, nax = ay + dy[j], ax + dx[j]
                        if 0 <= nay < R and 0 <= nax < C:
                            tmpDis = abs(nay - ny) + abs(nax - nx)
                            if tmpDis < minDis:
                                minDis = tmpDis
                                minIdx = j
                    nay, nax = ay + dy[minIdx], ax + dx[minIdx] # cIdx 아두이노를 nay, nax 위치로 이동
                    if board[nay][nax] == 'I':
                        print('kraj %s' % (i + 1))
                        return
                    else: # 무조건 다 이동 후 정리해줌
                        board[ay][ax] = '.'
                        cBoard[nay][nax].append(cIdx)
            for j in range(R):
                for k in range(C):
                    l = len(cBoard[j][k])
                    if l == 1:
                        cIdx = cBoard[j][k][0]
                        board[j][k] = cIdx
                        crazy[cIdx] = [j, k]
                    if l > 1:
                        board[j][k] = '.'
                        for cIdx in cBoard[j][k]:
                            crazy[cIdx] = None
                    cBoard[j][k] = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'I' or board[i][j] == '.':
                print(board[i][j], end='')
            else:
                print('R', end='')
        print()


if __name__ == '__main__':
    main()
