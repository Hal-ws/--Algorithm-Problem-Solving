import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for i in range(N):
        board.append(list(map(str, sys.stdin.readline()[:M])))
    pChk = [0] * N
    vChk = [0] * M
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'X':
                pChk[i] = 1
                vChk[j] = 1
    print(max(N - sum(pChk), M - sum(vChk)))


if __name__ == '__main__':
    main()
