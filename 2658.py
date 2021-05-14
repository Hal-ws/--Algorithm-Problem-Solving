import sys


def main():
    board = []
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    for _ in range(10):
        board.append(list(sys.stdin.readline()[:10]))
    visit = [[0 for j in range(10)] for i in range(10)]
    for i in range(10):
        flag = 0
        for j in range(10):
            if board[i][j] == '1':
                edges = [[i, j]]
                visit[i][j] = 1
                flag = 1
                break
        if flag:
            y, x = edges[0][0], edges[0][1]
            d = None
            for j in range(8):
                ny, nx = y + dy[j], x + dx[j]
                if 0 <= ny < 10 and 0 <= nx < 10 and board[ny][nx] == '1':
                    d = j
                    break
            if d == None:
                print(0)
                return
            break
    while 1: # 방향을 가지고 출발
        # 현재 방향으로 진행하는 다음 좌표
        print('y, x: %s, %s' %(y, x))
        for i in range(10):
            print(visit[i])
        print('----------------')
        ny, nx = y + dy[d], x + dx[d]
        endFlag = 1 # 더이상 진행 가능한 곳을 못찾으면 1 그대로 남는다
        # 지금 방향 그대로 진행 가능할때
        if 0 <= ny < 10 and 0 <= nx < 10 and board[ny][nx] == '1':
            if visit[ny][nx] == 0:
                visit[ny][nx] = 1
                y, x = ny, nx
                endFlag = 0
            else:
                break
        else: # 진행 불가. 꺾어줘야함 (현재 위치인 y, x 가 꼭지점)
            cFlag = 0
            for i in range(d + 1, 8):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < 10 and 0 <= nx < 10 and board[ny][nx] == '1' and visit[ny][nx] == 0: # 꺾일수 있는 점인거 확인
                    visit[ny][nx] = 1
                    edges.append([y, x])
                    y, x = ny, nx
                    cFlag = 1
                    endFlag = 0
                    d = i
                    break
            if cFlag == 0:
                for i in range(d):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < 10 and 0 <= nx < 10 and board[ny][nx] == '1' and visit[ny][nx] == 0:
                        visit[ny][nx] = 1
                        edges.append([y, x])
                        y, x = ny, nx
                        endFlag = 0
                        d = i
                        break
        if endFlag:
            break
    print(edges)


if __name__ == '__main__':
    main()
