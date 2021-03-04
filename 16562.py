import sys
from collections import deque


def main():
    global N, M, money, friends, relation
    N, M, K = map(int, sys.stdin.readline().split())
    money = [0] + list(map(int, sys.stdin.readline().split()))
    relation = [[] for i in range(N + 1)]
    friends = [0] * (N + 1) # 친구가 됐으면 1로 표시
    tPrice = 0
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        relation[a].append(b)
        relation[b].append(a)
    for i in range(1, N + 1):
        if friends[i] == 0: # 아직 친구가 아님
            tPrice += bfs(i)
    if K < tPrice:
        print('Oh no')
    else:
        print(tPrice)


def bfs(start):
    global N, M, money, friends, relation
    q = deque()
    visit = [0] * (N + 1)
    q.append(start)
    visit[start] = 1
    minPrice = money[start]
    while len(q) > 0:
        cur = q.popleft()
        friends[cur] = 1
        for nxt in relation[cur]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                q.append(nxt)
                if money[nxt] < minPrice:
                    minPrice = money[nxt]
    return minPrice


if __name__ == '__main__':
    main()
