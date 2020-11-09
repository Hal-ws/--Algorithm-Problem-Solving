from collections import deque


def main():
    N, K = map(int, input().split())
    q = deque()
    visitChk = [-1] * 100001 # 방문할때까지 걸린 초도 기록
    visitChk[N] = 1
    if N == K:
        print(0)
        print(1)
        return 0
    if N > 0:
        visitChk[N - 1] = 1
        q.append([N - 1, 1])
    if N <= 50000:
        visitChk[2 * N] = 1
        q.append([2 * N, 1])
    if N < 100000:
        visitChk[N + 1] = 1
        q.append([N + 1, 1])
    bfs(q, K, visitChk)


def bfs(q, K, visitChk):
    while len(q) > 0:
        if q[0][0] > 0 and (visitChk[q[0][0] - 1] == -1 or visitChk[q[0][0] - 1] >= q[0][1] + 1):
            q.append([q[0][0] - 1, q[0][1] + 1])
            visitChk[q[0][0] - 1] = q[0][1] + 1 # 방문할때 걸리는 최소시간 기록
        if q[0][0] < 100000 and (visitChk[q[0][0] + 1] == -1 or visitChk[q[0][0] + 1] >= q[0][1] + 1):
            q.append([q[0][0] + 1, q[0][1] + 1])
            visitChk[q[0][0] + 1] = q[0][1] + 1
        if q[0][0] <= 50000 and (visitChk[q[0][0] * 2] == -1 or visitChk[q[0][0] * 2] >= q[0][1] + 1):
            q.append([q[0][0] * 2, q[0][1] + 1])
            visitChk[q[0][0] * 2] = q[0][1] + 1
        if q[0][0] == K:
            minTime = q[0][1]
            break
        del q[0]
    cases = 0
    for i in range(len(q)):
        if q[i][0] == K and q[i][1] == minTime:
            cases += 1
        if q[i][1] > minTime:
            break
    print(minTime)
    print(cases)


if __name__ == "__main__":
    main()
