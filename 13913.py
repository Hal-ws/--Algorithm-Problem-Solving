from collections import deque


def main():
    N, K = map(int, input().split())
    q = deque()
    visitChk = [0] * 100001
    paths = [0] * 100001 # 어디에서 왔는지만 기록한다
    visitChk[N] = 1
    if N == K:
        print(0)
        print('%s %s' %(N, K))
        return 0
    if N > 0:
        visitChk[N - 1] = 1
        q.append([N - 1, 1])
        paths[N - 1] = N
    if N <= 50000:
        visitChk[2 * N] = 1
        q.append([2 * N, 1])
        paths[N * 2] = N
    if N < 100000:
        if visitChk[N + 1] == 0:
            visitChk[N + 1] = 1
            q.append([N + 1, 1])
            paths[N + 1] = N
    bfs(q, N, K, visitChk, paths)


def bfs(q, N, K, visitChk, paths):
    while len(q) > 0:
        if q[0][0] > 0 and visitChk[q[0][0] - 1] == 0:
            q.append([q[0][0] - 1, q[0][1] + 1])
            visitChk[q[0][0] - 1] = 1
            paths[q[0][0] - 1] = q[0][0]
        if q[0][0] < 100000 and visitChk[q[0][0] + 1] == 0:
            q.append([q[0][0] + 1, q[0][1] + 1])
            visitChk[q[0][0] + 1] = 1
            paths[q[0][0] + 1] = q[0][0]
        if q[0][0] <= 50000 and visitChk[q[0][0] * 2] == 0:
            q.append([q[0][0] * 2, q[0][1] + 1])
            visitChk[q[0][0] * 2] = 1
            paths[q[0][0] * 2] = q[0][0]
        if q[0][0] == K:
            ans = q[0][1]
            break
        del q[0]
    print(ans)
    point = K
    path = [K]
    while paths[point] != N:
        path.append(paths[point])
        point = paths[point]
    path.append(N)
    for i in range(len(path) - 1, -1, -1):
        print(path[i], end = ' ')
    

if __name__ == "__main__":
    main()
