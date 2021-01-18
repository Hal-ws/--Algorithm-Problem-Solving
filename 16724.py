import sys


def main():
    global board, visit, N, M, ans
    N, M = map(int, sys.stdin.readline().split())
    board = []
    ans = 0
    cnt = 1
    for i in range(N):
        board.append(list(sys.stdin.readline()[:M]))
    visit = [[0 for j in range(M)] for i in range(N)]
    for i in range(N):
        for j in range(M):
            if visit[i][j] == 0:
                stack = [[i, j]]
                visit[i][j] = cnt
                gettarget(stack, cnt)
                cnt += 1
    print(ans)


def gettarget(stack, cnt):
    global board, visit, N, M, ans
    while 1:
        y, x = stack[-1][0], stack[-1][1]
        if board[y][x] == 'R':
            ny, nx = y, x + 1
        if board[y][x] == 'L':
            ny, nx = y, x - 1
        if board[y][x] == 'D':
            ny, nx = y + 1, x
        if board[y][x] == 'U':
            ny, nx = y - 1, x
        if visit[ny][nx] == 0: #한번도 방문한곳 없는곳으로 갈때
            stack.append([ny, nx])
            visit[ny][nx] = cnt
        else:
            if visit[ny][nx] == cnt: # 이번 순회에서 방문한 곳으로 되돌아갈때
                ans += 1
                flag = 1
                break
            else: # 다른 순회에서 방문한 곳으로 갈때
                flag = 0
                val = visit[ny][nx]
                break
    if flag:
        while len(stack) > 0:
            tmp = stack.pop()
            y, x = tmp[0], tmp[1]
            visit[y][x] = cnt
    else:
        while len(stack) > 0:
            tmp = stack.pop()
            y, x = tmp[0], tmp[1]
            visit[y][x] = val


if __name__ == '__main__':
    main()
