import sys
from collections import deque


def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        A, B = map(int, sys.stdin.readline().split())
        print(getans(A, B))

def getans(A, B):
    q = deque()
    visit = [0] * 10000
    q.append(['', A])
    dN = digit(A)
    visit[dN[0] * 1000 + dN[1] * 100 + dN[2] * 10 + dN[3]] = 1
    while len(q) > 0:
        c, num = q[0][0], q[0][1]
        if num == B:
            return c
        dV, sV = num * 2 % 10000, num - 1
        if visit[dV] == 0:
            visit[dV] = 1
            q.append([c + 'D', dV])
        if sV == -1:
            sV = 9999
        if visit[sV] == 0:
            visit[sV] = 1
            q.append([c + 'S', sV])
        dN = digit(num)
        lV = dN[1] * 1000 + dN[2] * 100 + dN[3] * 10 + dN[0]
        rV = dN[3] * 1000 + dN[0] * 100 + dN[1] * 10 + dN[2]
        if visit[lV] == 0:
            visit[lV] = 1
            q.append([c + 'L', lV])
        if visit[rV] == 0:
            visit[rV] = 1
            q.append([c + 'R', rV])
        q.popleft()


def digit(num):
    fth = num % 10
    num = num // 10
    thrd = num % 10
    num = num // 10
    scnd = num % 10
    fst = num // 10
    return [fst, scnd, thrd, fth]


if __name__ == '__main__':
    main()
