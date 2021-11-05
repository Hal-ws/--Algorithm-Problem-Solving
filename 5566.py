import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for _ in range(N):
        board.append(int(sys.stdin.readline()))
    hIdx = 0
    for i in range(M):
        mvCnt = int(sys.stdin.readline())
        hIdx += mvCnt
        if hIdx >= N - 1:
            hIdx = N - 1
        num = board[hIdx]
        hIdx += num
        if hIdx <= 0:
            hIdx = 0
        elif hIdx >= N - 1:
            hIdx = N - 1
        if hIdx == N - 1:
            print(i + 1)
            break


if __name__ == "__main__":
    main()
