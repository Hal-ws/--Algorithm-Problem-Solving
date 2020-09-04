import sys
from collections import deque

def main():
    M, N, K = map(int, sys.stdin.readline().split())
    paper = [[0 for i in range(N)] for j in range(M)]
    visitChk = [[0 for i in range(N)] for j in range(M)]
    for i in range(K):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        for j in range(x1, x2):
            for k in range(y1, y2):
                paper[M - k - 1][j] = 1
    answerList = []
    for i in range(M):
        for j in range(N):
            if visitChk[i][j] == 0 and paper[i][j] == 0:
                answerList.append(1 + bfs(i, j, N, M, paper, visitChk))
    answerList = sorted(answerList)
    print(len(answerList))
    for i in range(len(answerList)):
        print(answerList[i], end = ' ')


def bfs(i, j, N, M, paper, visitChk):
    visitChk[i][j] = 1
    area = 0
    q = deque([[i, j]])
    while len(q) > 0:
        if q[0][0] > 0:
            if visitChk[q[0][0] - 1][q[0][1]] == 0 and paper[q[0][0] - 1][q[0][1]] == 0:
                visitChk[q[0][0] - 1][q[0][1]] = 1
                q.append([q[0][0] - 1, q[0][1]])
                area += 1
        if q[0][0] < M - 1:
            if visitChk[q[0][0] + 1][q[0][1]] == 0 and paper[q[0][0] + 1][q[0][1]] == 0:
                visitChk[q[0][0] + 1][q[0][1]] = 1
                q.append([q[0][0] + 1, q[0][1]])
                area += 1
        if q[0][1] > 0:
            if visitChk[q[0][0]][q[0][1] - 1] == 0 and paper[q[0][0]][q[0][1] - 1] == 0:
                visitChk[q[0][0]][q[0][1] - 1] = 1
                q.append([q[0][0], q[0][1] - 1])
                area += 1
        if q[0][1] < N - 1:
            if visitChk[q[0][0]][q[0][1] + 1] == 0 and paper[q[0][0]][q[0][1] + 1] == 0:
                visitChk[q[0][0]][q[0][1] + 1] = 1
                q.append([q[0][0], q[0][1] + 1])
                area += 1
        q.popleft()
    return area

if __name__ == "__main__":
    main()
