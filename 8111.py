import sys
from _collections import deque


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        visit = [0] * (N + 1)
        q = deque()
        q.append(1)
        visit[1] = 1
        ans = 'BRAK'
        while len(q) > 0:
            val = q.popleft()
            if val % N == 0:
                ans = val
                break
            if visit[(val * 10) % N] == 0:
                q.append(val * 10)
                visit[(val * 10) % N] = 1
            if visit[(val * 10 + 1) % N] == 0:
                q.append(val * 10 + 1)
                visit[(val * 10 + 1) % N] = 1
        print(ans)


if __name__ == "__main__":
    main()
