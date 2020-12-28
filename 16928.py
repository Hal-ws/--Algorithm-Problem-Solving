from collections import deque
import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    event = [0 for i in range(101)]
    for i in range(N):
        start, end = map(int, sys.stdin.readline().split())
        event[start] = end
    for i in range(M):
        start, end = map(int, sys.stdin.readline().split())
        event[start] = end
    visit = [0] * 101
    q = deque()
    q.append([1, 0])
    visit[1] = 1
    while len(q) > 0:
        cur, mvCnt = q[0][0], q[0][1]
        if cur == 100:
            ans = mvCnt
            break
        for i in range(1, 7):
            nxt = cur + i
            if nxt <= 100 and visit[nxt] == 0:
                if event[nxt] == 0:
                    q.append([nxt, mvCnt + 1])
                    visit[nxt] = 1
                else:
                    q.append([event[nxt], mvCnt + 1])
                    visit[event[nxt]] = 1
        q.popleft()
    print(ans)


if __name__ == '__main__':
    main()
