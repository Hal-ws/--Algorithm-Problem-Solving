from collections import deque


def main():
    N = int(input())
    picture = []
    for i in range(N):
        picture.append(list(input()))
    lp = len(picture[0])
    picture2 = [[0 for i in range(lp)] for j in range(N)]
    for i in range(N):
        for j in range(lp):
            picture2[i][j] = picture[i][j]
            if picture2[i][j] == "G":
                picture2[i][j] = "R"
    visitChk1 = [[0 for i in range(lp)] for j in range(N)]
    visitChk2 = [[0 for i in range(lp)] for j in range(N)]
    ans1, ans2 = 0, 0
    for i in range(N):
        for j in range(lp):
            if visitChk1[i][j] == 0:
                ans1 += 1
                bfs(picture, visitChk1, i, j, N, lp)
    for i in range(N):
        for j in range(lp):
            if visitChk2[i][j] == 0:
                ans2 += 1
                bfs(picture2, visitChk2, i, j, N, lp)
    print('%s %s' %(ans1, ans2))


def bfs(picture, visitChk, y, x, N, lp):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = deque()
    q.append([y, x])
    visitChk[y][x] = 1
    while len(q) > 0:
        for i in range(4):
            if 0 <= q[0][1] + dx[i] < lp and 0 <= q[0][0] + dy[i] < N and visitChk[q[0][0] + dy[i]][q[0][1] + dx[i]] == 0 \
                    and picture[y][x] == picture[q[0][0] + dy[i]][q[0][1] + dx[i]]:
                visitChk[q[0][0] + dy[i]][q[0][1] + dx[i]] = 1
                q.append([q[0][0] + dy[i], q[0][1] + dx[i]])
        q.popleft()

if __name__ == "__main__":
    main()
