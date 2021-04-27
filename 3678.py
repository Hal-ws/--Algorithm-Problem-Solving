import sys


def main():
    global board, dy, dx
    c = int(sys.stdin.readline())
    dy, dx = [-1, -2, -1, 1, 2, 1], [1, 0, -1, -1, 0, 1]
    cntList = [0 ,1, 0, 0, 0, 0] # i번 자원이 사용된 횟수
    board = [[0 for j in range(163)] for i in range(325)]
    ansList = [0]
    board[162][81] = 1
    ansList.append(1)
    maxLayer = 82
    for l in range(2, maxLayer):
        print('%s layer start' %l)
        y, x = 162 + (l - 1) * dy[0], 81 + (l - 1) * dx[0] # 시작 위치
        board[y][x] = putNum(cntList, y, x)
        print('nth: %s' %(len(ansList)))
        print('y, x, board[y][x]: %s, %s, %s' %(y, x, board[y][x]))
        ansList.append(board[y][x])
        y, x = y - 1, x - 1
        for d in range(2, 8):
            d = d % 6
            print('d: %s' %d)
            if d == 2:
                maxMv = l - 2
            else:
                maxMv = l - 1
            for mv in range(maxMv): # l - 1씩 움직임
                board[y][x] = putNum(cntList, y, x)
                print('nth: %s' %(len(ansList)))
                print('y, x, board[y][x]: %s, %s, %s' %(y, x, board[y][x]))
                ansList.append(board[y][x])
                y, x = y + dy[d], x + dx[d]
    for i in range(c):
        n = int(sys.stdin.readline())
        print(ansList[n])


def putNum(cntList, y, x):
    global board, dy, dx
    canUse = []
    for rIdx in range(1, 6):
        flag = 0
        for i in range(6):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 325 and 0 <= nx < 163:
                if board[ny][nx] == rIdx:
                    flag = 1
                    break
        if flag == 0:
            canUse.append([cntList[rIdx], rIdx])
    canUse.sort()
    cntList[canUse[0][1]] += 1
    return canUse[0][1]


if __name__ == '__main__':
    main()
