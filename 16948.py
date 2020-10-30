from collections import deque


def main():
    N = int(input())
    dr = [-2, -2, 0, 0, 2, 2]
    dc = [-1, 1, -2, 2, -1, 1]
    r1, c1, r2, c2 = map(int, input().split())
    flag = 0
    visitChk = [[0 for i in range(N)] for j in range(N)]
    q = deque() # 마지막은 movingCnt
    q.append([r1, c1, 0])
    visitChk[r1][c1] = 1
    while len(q) > 0:
        if q[0][0] == r2 and q[0][1] == c2:
            ans = q[0][2]
            flag = 1
            break
        for i in range(6):
            if 0 <= q[0][0] + dr[i] < N and 0 <= q[0][1] + dc[i] < N:
                if visitChk[q[0][0] + dr[i]][q[0][1] + dc[i]] == 0:
                    visitChk[q[0][0] + dr[i]][q[0][1] + dc[i]] = 1
                    q.append([q[0][0] + dr[i], q[0][1] + dc[i], q[0][2] + 1])
        q.popleft()
    if flag:
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
