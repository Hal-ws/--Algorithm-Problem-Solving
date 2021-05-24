import sys


def main():
    global N, ans1, ans2, dy, dx #ans1: 검정칸 count. ans2: 흰칸 count
    N = int(sys.stdin.readline())
    board = []
    ans1, ans2 = 0, 0
    dy = [-1, -1, 1, 1]
    dx = [-1, 1, -1, 1]
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    for i in range(N): # 검정칸
        if i % 2 == 0:
            start = 0
        else:
            start = 1
        for j in range(start, N, 2):
            if board[i][j]:
                board[i][j] = 2
                backtracking(i, j, board, 1, 0)
                board[i][j] = 1
    for i in range(N): # 흰칸
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(start, N, 2):
            if board[i][j]:
                board[i][j] = 2
                backtracking(i, j, board, 1, 1)
                board[i][j] = 1
    print(ans1 + ans2)


def backtracking(y, x, board, cnt, flag):
    global N, ans1, ans2
    if flag == 0: # 검정칸
        if ans1 < cnt:
            ans1 = cnt
        for i in range(y, N):
            if i == y:
                start = x + 2
            else:
                if i % 2 == 0:
                    start = 0
                else:
                    start = 1
            for j in range(start, N, 2):
                if board[i][j] and chkPossible(i, j, board):
                    board[i][j] = 2
                    backtracking(i, j, board, cnt + 1, flag)
                    board[i][j] = 1
    else: # 흰칸
        if ans2 < cnt:
            ans2 = cnt
        for i in range(y, N):
            if i == y:
                start = x + 2
            else:
                if i % 2 == 0:
                    start = 1
                else:
                    start = 0
            for j in range(start, N, 2):
                if board[i][j] and chkPossible(i, j, board):
                    board[i][j] = 2
                    backtracking(i, j, board, cnt + 1, flag)
                    board[i][j] = 1


def chkPossible(y, x, board):
    global N, dy, dx
    for d in range(4):
        ny, nx = y, x
        while 1:
            ny, nx = ny + dy[d], nx + dx[d]
            if ny < 0 or ny > N - 1 or nx < 0 or nx > N - 1:
                break
            if board[ny][nx] == 2:
                return 0
    return 1



if __name__ == '__main__':
    main()
