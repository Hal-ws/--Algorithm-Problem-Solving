import sys


def main():
    N, L = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    ans = 0
    for i in range(N):
        ans += chkgaro(board, i, L, N)
        ans += chksero(board, i, L, N)
    print(ans)
    return 0


def chkgaro(board, idx, L, N):
    x = 0
    chk = [0] * N
    while x < N - 1: # x번째와 x + 1이 연결 가능한지 확인
        if board[idx][x] != board[idx][x + 1]:  # 경사로 설치필요
            if board[idx][x] - board[idx][x + 1] == -1:  # x - L + 1 ~ x 까지 설치해야함
                if x - L + 1 >= 0:  # x - L + 1부터 x 까지 설치
                    for j in range(x - L + 1, x + 1):
                        if chk[j] or board[idx][j] != board[idx][x]:
                            return 0
                    for j in range(x - L + 1, x + 1):
                        chk[j] = 1
                else:
                    return 0
            elif board[idx][x] - board[idx][x + 1] == 1:  # x + 1 ~ x + L 까지 설치
                if x + L < N:
                    for j in range(x + 1, x + L + 1):
                        if chk[j] or board[idx][j] != board[idx][x + 1]:
                            return 0
                    for j in range(x + 1, x + L + 1):
                        chk[j] = 1
                else:
                    return 0
            else:
                return 0
        x += 1
    return 1


def chksero(board, idx, L, N):
    y = 0
    chk = [0] * N
    while y < N - 1:  # y 번째와 y + 1이 연결 가능한지 확인
        if board[y][idx] != board[y + 1][idx]:
            if board[y][idx] - board[y + 1][idx] == -1:  # y - L + 1 ~ y 까지 설치
                if y - L + 1 >= 0:
                    for i in range(y - L + 1, y + 1):
                        if chk[i] or board[i][idx] != board[y][idx]:
                            return 0
                    for j in range(y - L + 1, y + 1):
                        chk[i] = 1
                else:
                    return 0
            elif board[y][idx] - board[y + 1][idx] == 1:  # y + 1 ~ y + L 까지 설치
                if y + L < N:
                    for i in range(y + 1, y + L + 1):
                        if chk[i] or board[i][idx] != board[y + 1][idx]:
                            return 0
                    for i in range(y + 1, y + L + 1):
                        chk[i] = 1
                else:
                    return 0
            else:
                return 0
        y += 1
    return 1


if __name__ == "__main__":
    main()
