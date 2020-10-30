import sys
from collections import deque
from copy import deepcopy

def main():
    N, M = map(int, sys.stdin.readline().split())
    room = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    areas = [0, 0] #각각 공간의 크기를 2번 공간부터 지정함.
    areaidx = 2
    for i in range(N):
        room.append(list(map(int, sys.stdin.readline()[:M])))
    ans = deepcopy(room)
    for i in range(N):
        for j in range(M):
            if room[i][j] == 0:
                q = deque([[i, j]])
                room[i][j] = areaidx
                temparea = 1
                while len(q) > 0:
                    for k in range(4):
                        y, x = q[0][0] + dy[k], q[0][1] + dx[k]
                        if 0 <= y < N and 0 <= x < M and room[y][x] == 0:
                            room[y][x] = areaidx
                            q.append([y, x])
                            temparea += 1
                    q.popleft()
                areas.append(temparea)
                areaidx += 1
    for i in range(N):
        for j in range(M):
            if ans[i][j] == 1:
                ans[i][j] += getans(room, areas, i, j, areaidx, N, M)
    for i in range(N):
        for j in range(M):
            print(ans[i][j], end='')
        print()


def getans(room, areas, y, x, areaidx, N, M):
    visitChk = [0] * areaidx
    poss = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        if 0 <= y + dy[i] < N and 0 <= x + dx[i] < M and room[y + dy[i]][x + dx[i]] != 1:
            if visitChk[areas[room[y + dy[i]][x + dx[i]]]] == 0:
                visitChk[room[y + dy[i]][x + dx[i]]] = 1
                poss += areas[room[y + dy[i]][x + dx[i]]]
    return poss


if __name__ == "__main__":
    main()
