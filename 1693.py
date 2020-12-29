from collections import deque
import sys


def main():
    global prime
    T = int(sys.stdin.readline())
    prime = prime_list(10000)
    for i in range(T):
        start, end = map(int, sys.stdin.readline().split())
        print(bfs(start, end))


def prime_list(n):
    sieve = [1] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i+i, n, i):
                sieve[j] = 0
    return sieve


def bfs(start, end):
    global prime
    q = deque()
    q.append([start, 0])
    visit = [0] * 10000
    visit[q[0][0]] = 1
    while len(q) > 0:
        cur = q[0][0]
        if cur == end:
            return q[0][1]
        for i in range(4):
            num = str(cur)
            tmpList = change(num, i)
            for nxt in tmpList:
                if visit[nxt] == 0 and prime[nxt] == 1:
                    visit[nxt] = 1
                    q.append([nxt, q[0][1] + 1])
        q.popleft()
    return "Impossible"


def change(num, idx):
    result = []
    if idx == 0:
        for i in range(1, 10):
            result.append(int(str(i) + num[1] + num[2] + num[3]))
    if idx == 1:
        for i in range(10):
            result.append(int(num[0] + str(i) + num[2] + num[3]))
    if idx == 2:
        for i in range(10):
            result.append(int(num[0] + num[1] + str(i) + num[3]))
    if idx == 1:
        for i in range(10):
            result.append(int(num[0] + num[1] + num[2] + str(i)))
    return result




if __name__ == '__main__':
    main()
