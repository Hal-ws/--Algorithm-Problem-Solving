import sys
from collections import deque


def main():
    global board, dy, dx
    cnt = 0
    board = []
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(12):
        board.append(list(sys.stdin.readline()[:6]))
    while 1:
        flag = 0 #
        visit = [[0 for j in range(6)] for i in range(12)]
        for i in range(12):
            for j in range(6):
                if visit[i][j] == 0 and board[i][j] != '.':
                    puyo = bfs([i, j], visit)
                    if len(puyo) >= 4:
                        flag = 1 #터뜨릴수 있는거 있는것 확인
                        for k in range(len(puyo)):
                            board[puyo[k][0]][puyo[k][1]] = '0' #터짐
        down()
        if flag: #터지는게 일어났으면 cnt +
            cnt += 1
        else:
            break
    print(cnt)


def down():
    global board
    for j in range(6):
        flag, sIdx, eIdx = 0, -1, -1
        for i in range(11, -1, -1):
            if board[i][j] == '0':
                sIdx = i
                flag = 1
                break
        if flag:
            for i in range(sIdx, -1, -1):
                if board[i][j] != '0':
                    eIdx = i + 1
                    break
                elif i == 0: # 빈칸이지만 위 끝까지 간경우
                    eIdx = i
            dis = sIdx - eIdx + 1
            for i in range(eIdx - 1, -1, -1):
                board[i + dis][j] = board[i][j]
            for i in range(dis):
                board[i][j] = '.'


def bfs(pos, visit):
    global board, dy, dx
    y, x = pos[0], pos[1]
    color = board[y][x]
    visit[y][x] = 1
    q = deque()
    q.append([y, x])
    result = [[y, x]]
    while len(q) > 0:
        y, x = q[0][0], q[0][1]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 12 and 0 <= nx < 6:
                if visit[ny][nx] == 0 and board[ny][nx] == color:
                    visit[ny][nx] = 1
                    q.append([ny, nx])
                    result.append([ny, nx])
        q.popleft()
    return result


if __name__ == '__main__':
    main()
