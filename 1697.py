import sys
from collections import deque


def main():
    N, K = map(int, sys.stdin.readline().split())
    q = deque()
    q.append(['m', N - 1])
    q.append(['p', N + 1])
    q.append(['d', 2 * N])
    print(bfs(q, N, K))

def bfs(q, N, K):
    if N == K:
        return 0
    if q[0][1] == K or q[1][1] == K or q[2][1] == K:
        return 1
    lb, la = 3, 3
    seconds = 1
    while 1:
        for i in range(lb):
            if q[i][0] == 'm':
                q.append(['m', q[i][1] - 1])
                q.append(['d', q[i][1] * 2])
                la += 2
                if q[la - 2][1] == K or q[la - 1][1] == K:
                    return seconds + 1
            elif q[i][0] == 'p':
                q.append(['p', q[i][1] + 1])
                q.append(['d', q[i][1] * 2])
                la += 2
                if q[la - 2][1] == K or q[la - 1][1] == K:
                    return seconds + 1
            else:
                q.append(['m', q[i][1] - 1])
                q.append(['p', q[i][1] + 1])
                q.append(['d', q[i][1] * 2])
                la += 3
                if q[la - 3][1] == K or q[la - 2][1] == K or q[la - 1][1] == K:
                    return seconds + 1
        for i in range(lb):
            q.popleft()
            la -= 1
        lb = la
        seconds += 1
    print(seconds)

if __name__ == "__main__":
    main()