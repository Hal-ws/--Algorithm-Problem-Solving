import sys
from queue import deque


def main():
    global N, bridges
    N, M = map(int, sys.stdin.readline().split())
    bridges = [[] for i in range(N + 1)]
    left, right = 0, 0
    answer = 0
    for i in range(M):
        a, b, w = map(int, sys.stdin.readline().split())
        bridges[a].append([b, w])
        bridges[b].append([a, w])
        if w > right:
            right = w
    right += 1
    start, end = map(int, sys.stdin.readline().split())
    while left <= right:
        mid = (left + right) // 2
        if bfs(start, end, mid): # 최대 중량이 mid로 가능함
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
    print(answer)


def bfs(start, end, W):
    global N, bridges
    visit = [0] * (N + 1)
    q = deque()
    q.append(start)
    visit[start] = 1
    while len(q) > 0:
        cur = q.popleft()
        if cur == end:
            return 1
        for tmp in bridges[cur]:
            nxtCity, posW = tmp[0], tmp[1]
            if posW >= W and visit[nxtCity] == 0:
                visit[nxtCity] = 1
                q.append(nxtCity)
    return 0


if __name__ == '__main__':
    main()
