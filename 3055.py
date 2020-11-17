import sys
from collections import deque


def main():
    R, C = map(int, sys.stdin.readline().split())
    forest = []
    water = deque()
    for i in range(R):
        forest.append(list(sys.stdin.readline()[:C]))
        for j in range(C):
            if forest[i][j] == "S":
                start = [i, j]
            if forest[i][j] == "*":
                water.append([i, j])
    print(bfs(forest, water, start, R, C))


def bfs(forest, water, start, R, C):
    q = deque([[start[0], start[1], 0]]) # i, j 위치, 시간 저장
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    visited = [[0 for i in range(C)] for j in range(R)]
    visited[start[0]][start[1]] = 1
    ans, endflag = 0, 0
    while len(q) > 0:
        flooded(forest, water, R, C, dx, dy)
        l = len(q)
        for j in range(l):
            for i in range(4):
                if 0 <= q[0][0] + dy[i] < R and 0 <= q[0][1] + dx[i] < C:
                    if visited[q[0][0] + dy[i]][q[0][1] + dx[i]] == 0:
                        if forest[q[0][0] + dy[i]][q[0][1] + dx[i]] == ".":
                            visited[q[0][0] + dy[i]][q[0][1] + dx[i]] = 1
                            forest[q[0][0] + dy[i]][q[0][1] + dx[i]] = "S"
                            q.append([q[0][0] + dy[i], q[0][1] + dx[i], q[0][2] + 1])
                        if forest[q[0][0] + dy[i]][q[0][1] + dx[i]] == "D":
                            endflag = 1
                            ans = q[0][2] + 1
                            break
            del q[0]
        if endflag:
            break
    if ans == 0:
        return "KAKTUS"
    else:
        return ans


def flooded(forest, water, R, C, dx, dy):
    l = len(water)
    for i in range(l):
        for j in range(4):
            if 0 <= water[i][1] + dx[j] < C and 0 <= water[i][0] + dy[j] < R:
                if forest[water[i][0] + dy[j]][water[i][1] + dx[j]] == ".":
                    forest[water[i][0] + dy[j]][water[i][1] + dx[j]] = "*"
                    water.append([water[i][0] + dy[j], water[i][1] + dx[j]])
    for i in range(l):
        del water[0]


if __name__ == "__main__":
    main()
