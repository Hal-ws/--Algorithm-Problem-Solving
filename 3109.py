import sys


def main():
    global R, C, dy, dx, board, visit, flag, ansPath
    R, C = map(int, sys.stdin.readline().split())
    dy = [-1, 0, 1]
    dx = [1, 1, 1]
    board = []
    ans = 0
    for i in range(R):
        board.append(list(sys.stdin.readline()[:C]))
    visit = [[0 for j in range(C)] for i in range(R)]
    for i in range(R):
        flag = 0
        ansPath = []
        dfs([[i, 0]])
        if ansPath != []:
            for p in ansPath:
                visit[p[0]][p[1]] = 2 # 파이프는 2로 표시
            ans += 1
    print(ans)


def dfs(path):
    global R, C, dy, dx, board, visit, flag, ansPath
    y, x = path[-1][0], path[-1][1]
    if flag:
        return # 답을 찾았으면 종료
    if x == C - 1: # 답 찾음
        ansPath = [path[i] for i in range(len(path))]
        flag = 1
        return
    pFlag = 0
    for i in range(3):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < R and 0 <= nx < C and visit[ny][nx] == 0 and board[ny][nx] != 'x':
            pFlag = 1
            path.append([ny, nx])
            visit[ny][nx] = 1
            dfs(path)
            visit[ny][nx] = 0
            path.pop()
    if pFlag == 0:
        board[y][x] = 'x'
    else:
        wFlag = 1
        for i in range(3):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if board[ny][nx] == '.':
                    wFlag = 0
                    break
        if wFlag:
            board[y][x] = 'x'


if __name__ == '__main__':
    main()
