import sys
from collections import deque
def main():
    while True:
        w, h = map(int, sys.stdin.readline().split())
        if w + h == 0:
            break
        island = []
        for i in range(h):
            island.append(list(map(int, sys.stdin.readline().split())))
        print(cntislands(w, h, island))


def cntislands(w, h, island):
    visitChk = [[0 for i in range(w)] for j in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if visitChk[i][j] == 0 and island[i][j] == 1:
                cnt += 1
                visitChk[i][j] = 1
                q = deque([[i, j]])
                while len(q) > 0:
                    if q[0][0] > 0 :
                        if visitChk[q[0][0] - 1][q[0][1]] == 0 and island[q[0][0] - 1][q[0][1]] == 1:
                            q.append([q[0][0] - 1, q[0][1]])
                            visitChk[q[0][0] - 1][q[0][1]] = 1
                        if q[0][1] > 0:
                            if visitChk[q[0][0] - 1][q[0][1] - 1] == 0 and island[q[0][0] - 1][q[0][1] - 1] == 1:
                                q.append([q[0][0] - 1, q[0][1] - 1])
                                visitChk[q[0][0] - 1][q[0][1] - 1] = 1
                        if q[0][1] < w - 1:
                            if visitChk[q[0][0] - 1][q[0][1] + 1] == 0 and island[q[0][0] - 1][q[0][1] + 1] == 1:
                                q.append([q[0][0] - 1, q[0][1] + 1])
                                visitChk[q[0][0] - 1][q[0][1] + 1] = 1
                    if q[0][0] < h - 1:
                        if visitChk[q[0][0] + 1][q[0][1]] == 0 and island[q[0][0] + 1][q[0][1]] == 1:
                            q.append([q[0][0] + 1, q[0][1]])
                            visitChk[q[0][0] + 1][q[0][1]] = 1
                        if q[0][1] > 0:
                            if visitChk[q[0][0] + 1][q[0][1] - 1] == 0 and island[q[0][0] + 1][q[0][1] - 1] == 1:
                                q.append([q[0][0] + 1, q[0][1] - 1])
                                visitChk[q[0][0] + 1][q[0][1] - 1] = 1
                        if q[0][1] < w - 1:
                            if visitChk[q[0][0] + 1][q[0][1] + 1] == 0 and island[q[0][0] + 1][q[0][1] + 1] == 1:
                                q.append([q[0][0] + 1, q[0][1] + 1])
                                visitChk[q[0][0] + 1][q[0][1] + 1] = 1
                    if q[0][1] > 0:
                        if visitChk[q[0][0]][q[0][1] - 1] == 0 and island[q[0][0]][q[0][1] - 1] == 1:
                            q.append([q[0][0], q[0][1] - 1])
                            visitChk[q[0][0]][q[0][1] - 1] = 1
                    if q[0][1] < w - 1:
                        if visitChk[q[0][0]][q[0][1] + 1] == 0 and island[q[0][0]][q[0][1] + 1] == 1:
                            q.append([q[0][0], q[0][1] + 1])
                            visitChk[q[0][0]][q[0][1] + 1] = 1
                    q.popleft()
    return cnt

if __name__ == "__main__":
    main()
