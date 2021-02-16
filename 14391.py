import sys
from itertools import product


def main():
    N, M = map(int, sys.stdin.readline().split())
    cases = list(product([0, 1], repeat=N * M))
    board = []
    ans = 0
    for i in range(N):
        board.append(sys.stdin.readline()[:M])
    for case in cases:
        sign = [[0 for j in range(M)] for i in range(N)] # 0은 가로, 1은 세로
        for i in range(N * M):
            sign[i // M][i % M] = case[i]
        visit = [[0 for j in range(M)] for i in range(N)]
        val = 0
        for i in range(N):
            for j in range(M):
                if visit[i][j] == 0:
                    if sign[i][j] == 0: # 가로로 갈때
                        tmp = ''
                        for k in range(j, M):
                            if visit[i][k] == 0 and sign[i][k] == 0: # 빈칸이고 계속 가로로 갈때
                                tmp += board[i][k]
                                visit[i][k] = 1
                            else:
                                break
                        val += int(tmp)
                    else: # 세로로 갈때
                        tmp = ''
                        for k in range(i, N):
                            if visit[k][j] == 0 and sign[k][j] == 1: # 빈칸이고 계속 세로로 갈때
                                tmp += board[k][j]
                                visit[k][j] = 1
                            else:
                                break
                        val += int(tmp)
        if ans < val:
            ans = val
    print(ans)


if __name__ == '__main__':
    main()
