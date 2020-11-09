from collections import deque


def main():
    N, K = map(int, input().split())
    q = deque()
    visitChk = [0] * 200001
    visitChk[N] = 1
    if N == K:
        print(0)
        return 0
    if N > 0:
        visitChk[N - 1] = 1
        q.append([N - 1, 1])
    if N < 100000:
        visitChk[N + 1] = 1
        q.append([N + 1, 1])
        visitChk[2 * N] = 1
        q.append([2 * N, 1])
    print(bfs(q, K, visitChk))

def bfs(q, K, visitChk):
    while len(q) > 0:
        if q[0][0] > 0 and visitChk[q[0][0] - 1] == 0:
            q.append([q[0][0] - 1, q[0][1] + 1])
            visitChk[q[0][0] - 1] = 1
        if q[0][0] < 200000 and visitChk[q[0][0] + 1] == 0:
            q.append([q[0][0] + 1, q[0][1] + 1])
            visitChk[q[0][0] + 1] = 1
        if q[0][0] <= 100000 and visitChk[q[0][0] * 2] == 0:
            q.append([q[0][0] * 2, q[0][1] + 1])
            visitChk[q[0][0] * 2] = 1
        if q[0][0] == K:
            return q[0][1]
        del q[0]


if __name__ == "__main__":
    main()
