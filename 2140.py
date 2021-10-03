import sys


def main():
    N = int(sys.stdin.readline())
    if N == 1:
        print(0)
        return
    board = []
    for _ in range(N):
        board.append(list(sys.stdin.readline()[:N]))
    for i in range(N):
        for j in range(N):
            if 48 <= ord(board[i][j]) <= 57:
                board[i][j] = int(board[i][j])
    for x in range(N):
        cnt = 0
        for nx in range(x - 1, x + 2):
            if 0 <= nx < N and board[1][nx] == '*':
                cnt += 1
        if cnt < board[0][x]:
            for nx in range(x - 1, x + 2):
                if 0 <= nx < N and board[1][nx] == '#':
                    if cnt < board[0][x]:
                        board[1][nx] = '*'
                        cnt += 1
                    else:
                        board[1][nx] = ' '
        else:
            for nx in range(x - 1, x + 2):
                if 0 <= nx < N and board[1][nx] == '#':
                    board[1][nx] = ' '
        cnt = 0
        for nx in range(x - 1, x + 2):
            if 0 <= nx < N and board[N - 2][nx] == '*':
                cnt += 1
        if cnt < board[N - 1][x]:
            for nx in range(x - 1, x + 2):
                if 0 <= nx < N and board[N - 2][nx] == '#':
                    if cnt < board[N - 1][x]:
                        board[N - 2][nx] = '*'
                        cnt += 1
                    else:
                        board[N - 2][nx] = ' '
        else:
            for nx in range(x - 1, x + 2):
                if 0 <= nx < N and board[N - 2][nx] == '#':
                    board[N - 2][nx] = ' '
    for y in range(N):
        cnt = 0
        for ny in range(y - 1, y + 2):
            if 0 <= ny < N and board[ny][1] == '*':
                cnt += 1
        if cnt < board[y][0]:
            for ny in range(y - 1, y + 2):
                if 0 <= ny < N and board[ny][1] == '#':
                    if cnt < board[y][0]:
                        board[ny][1] = '*'
                        cnt += 1
                    else:
                        board[ny][1] = ' '
        else:
            for ny in range(y - 1, y + 2):
                if 0 <= ny < N and board[ny][1] == '#':
                    board[ny][1] = ' '
        cnt = 0
        for ny in range(y - 1, y + 2):
            if 0 <= ny < N and board[ny][N - 2] == '*':
                cnt += 1
        if cnt < board[y][N - 1]:
            for ny in range(y - 1, y + 2):
                if 0 <= ny < N and board[ny][N - 2] == '#':
                    if cnt < board[y][N - 1]:
                        board[ny][N - 2] = '*'
                        cnt += 1
                    else:
                        board[ny][N - 2] = ' '
        else:
            for ny in range(y - 1, y + 2):
                if 0 <= ny < N and board[ny][N - 2] == '#':
                    board[ny][N - 2] = ' '
    ans = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == '#' or board[i][j] == '*':
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
