import sys
from itertools import combinations
from math import inf


def main():
    N = int(sys.stdin.readline())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    ans = inf
    for i in range(1, N): # a팀의 인원이 1명~N-1명까지 나오는 경우의 수를 계산함
        ans = min(ans, getDiff(board, i, N))
    print(ans)


def getDiff(board, aMember, N):
    members = [i for i in range(N)]
    cases = combinations(members, aMember)
    result = inf
    for case in cases:
        teamA = [0] * N
        aScore, bScore = 0, 0
        for num in case:
            teamA[num] = 1
        for i in range(N):
            for j in range(N):
                if teamA[i] == teamA[j] == 1:
                    aScore += board[i][j]
                if teamA[i] == teamA[j] == 0:
                    bScore += board[i][j]
        result = min(result, abs(aScore - bScore))
    return result


if __name__ == "__main__":
    main()
