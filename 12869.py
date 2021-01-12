import sys
from _collections import deque

def main():
    N = int(sys.stdin.readline())
    scv = list(map(int, sys.stdin.readline().split()))
    two, three = [[9, 3], [3, 9]], [[9, 3, 1], [9, 1, 3], [3, 9, 1], [3, 1, 9], [1, 9, 3], [1, 3, 9]]
    if N == 1:
        ans = scv[0] // 9
        scv[0] = scv[0] % 9
        if scv[0] > 0:
            ans += 1
    elif N == 2:
        visit = [[0 for i in range(61)] for j in range(61)]
        q = deque()
        q.append(scv + [0])
        visit[scv[0]][scv[1]] = 1
        while len(q) > 0:
            first, second, cnt = q[0][0], q[0][1], q[0][2]
            if first == 0 and second == 0:
                ans = cnt
                break
            for i in range(2):
                nxt = [-1, -1]
                nxt[0] = first - two[i][0]
                if nxt[0] <= 0:
                    nxt[0] = 0
                nxt[1] = second - two[i][1]
                if nxt[1] <= 0:
                    nxt[1] = 0
                if visit[nxt[0]][nxt[1]] == 0:
                    visit[nxt[0]][nxt[1]] = 1
                    q.append([nxt[0], nxt[1], cnt + 1])
            q.popleft()
    else:
        visit = [[[0 for k in range(61)] for j in range(61)] for i in range(61)]
        q = deque()
        q.append(scv + [0])
        visit[scv[0]][scv[1]][scv[2]] = 1
        while len(q) > 0:
            first, second, third, cnt = q[0][0], q[0][1], q[0][2] ,q[0][3]
            if first == second == third == 0:
                ans = cnt
                break
            for i in range(6):
                nxt = [-1, -1, -1]
                nxt[0] = first - three[i][0]
                if nxt[0] <= 0:
                    nxt[0] = 0
                nxt[1] = second - three[i][1]
                if nxt[1] <= 0:
                    nxt[1] = 0
                nxt[2] = third - three[i][2]
                if nxt[2] <= 0:
                    nxt[2] = 0
                if visit[nxt[0]][nxt[1]][nxt[2]] == 0:
                    visit[nxt[0]][nxt[1]][nxt[2]] = 1
                    q.append([nxt[0], nxt[1], nxt[2], cnt + 1])
            q.popleft()
    print(ans)


if __name__ == '__main__':
    main()
