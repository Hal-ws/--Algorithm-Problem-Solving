import sys
from collections import deque


def main():
    global matrix
    N = int(sys.stdin.readline())
    matrix = []
    answer = 1000000 * 16 + 1
    for i in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    dp = [[-1 for j in range(N)] for i in range(pow(2, N))]
    q = deque()
    q.append([1, 0]) # path, 현재 node 저장
    dp[1][0] = 0
    while len(q) > 0:
        tmp = q.popleft()
        path, cNode = tmp[0], tmp[1]
        for i in range(N):
            if matrix[cNode][i] != 0:
                nxtNode = pow(2, i) # nxtNode를 2진법으로 표현
                nPath = path | nxtNode
                cost = dp[path][cNode] + matrix[cNode][i]
                if nPath != path:
                    if dp[nPath][i] == -1 or cost < dp[nPath][i]:
                        dp[nPath][i] = cost
                        q.append([nPath, i])
    for i in range(1, N):
        if matrix[i][0] != 0 and dp[pow(2, N) - 1][i] != -1:
            cost = dp[pow(2, N) - 1][i] + matrix[i][0]
            if cost < answer:
                answer = cost
    print(answer)


if __name__ == '__main__':
    main()
