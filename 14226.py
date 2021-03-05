import sys
from collections import deque


def main():
    N = int(sys.stdin.readline())
    visit = [[0 for j in range(2001)] for i in range(2001)]
    visit[1][0] = 1
    q = deque()
    q.append([1, 0, 0]) # 이모티콘 길이, 클립보드에 저장된 길이
    while len(q) > 0:
        tmp = q.popleft()
        l, clip, t = tmp[0], tmp[1], tmp[2]
        if l == N:
            print(t)
            break
        if l + clip <= 2000 and visit[l + clip][clip] == 0:
            visit[l + clip][clip] = 1
            q.append([l + clip, clip, t + 1])
        if visit[l][l] == 0:
            visit[l][l] = 1
            q.append([l, l, t + 1])
        if l - 1 >= 0 and visit[l - 1][clip] == 0:
            visit[l - 1][clip] = 1
            q.append([l - 1, clip, t + 1])


if __name__ == '__main__':
    main()
