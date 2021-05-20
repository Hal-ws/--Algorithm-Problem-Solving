import sys
from math import inf
from _collections import deque


def main():
    N = int(sys.stdin.readline())
    matrix = []
    ans = inf
    for i in range(N):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    dp = [[inf for j in range(pow(2, N))] for i in range(N)]
    q = deque()
    for i in range(N):
        q.append([i, pow(2, i)])
        dp[i][pow(2, i)] = 0
    while len(q) > 0:
        print('q: %s' %q)
        tmp = q.popleft()
        cur, path = tmp[0], tmp[1]
        if path == pow(2, N) - 1:
            if dp[cur][path] < ans:
                ans = dp[cur][path]
        else:
            for nxt in range(N):
                if matrix[cur][nxt] != 0: # 연결되는 길이 있을 때
                    if path | pow(2, nxt) == path + pow(2, nxt): #현재 path 에서 nxt번째가 방문 안된거일때
                        if dp[cur][path] + matrix[cur][nxt] < dp[nxt][path + pow(2, nxt)]: # 더 짧게 방문할 수 있을 때
                            dp[nxt][path + pow(2, nxt)] = dp[cur][path] + matrix[cur][nxt]
                            q.append([nxt, path + pow(2, nxt)])
    print(ans)



if __name__ == '__main__':
    main()
