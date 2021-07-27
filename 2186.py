import sys


def main():
    N, M, K = map(int, sys.stdin.readline().split())
    board = []
    aList = [[] for i in range(26)]
    for i in range(N):
        board.append(list(sys.stdin.readline()[:M]))
    target = sys.stdin.readline()
    l = len(target)
    target = target[:l - 1]
    l -= 1
    answer = 0
    for i in range(N):
        for j in range(M):
            aList[ord(board[i][j]) - 65].append([i, j])
    dp = [[0 for j in range(M)] for i in range(N)]
    for sPos in aList[ord(target[0]) - 65]: # 시작 좌표들
        dfs(sPos, 0, l, dp, target, aList, K)
    for sPos in aList[ord(target[0]) - 65]:
        answer += dp[sPos[0]][sPos[1]]
    print(answer)


def dfs(pos, idx, l, dp, target, aList, K):
    y, x = pos[0], pos[1]
    if idx == l - 1: # 끝까지 도달함
        dp[y][x] = 1
        return 1
    nxtC = target[idx + 1] # 다음 문자
    for nxtPos in aList[ord(nxtC) - 65]: # 다음 좌표
        if pickable(pos, nxtPos, K): # 이동 가능한 좌표
            ny, nx = nxtPos[0], nxtPos[1]
            if dp[ny][nx] != 0: #이미 도달한 값이 있을때. 더이상 진행안함
                dp[y][x] += dp[ny][nx]
            else:
                dp[y][x] += dfs(nxtPos, idx + 1, l, dp, target, aList, K)
    return dp[y][x]


def pickable(p1, p2, K): # 고를 수 있는지 확인
    y1, x1, y2, x2 = p1[0], p1[1], p2[0], p2[1]
    if y1 == y2 and x1 == x2: #동일 지점은 선택 불가
        return 0
    if y1 == y2 and abs(x2 - x1) <= K:
        return 1
    if x1 == x2 and abs(y2 - y1) <= K:
        return 1
    return 0


if __name__ == '__main__':
    main()
