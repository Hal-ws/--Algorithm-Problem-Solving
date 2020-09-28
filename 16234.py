import sys
from queue import deque

def main():
    N, L, R = map(int, sys.stdin.readline().split())
    people = []
    cnt = 0
    for i in range(N):
        people.append(list(map(int, sys.stdin.readline().split())))
    while True:
        if moving(N, people, L, R):
            cnt += 1
        else:
            break
    print(cnt)


def moving(N, people, L, R):
    visitChk = [[0 for i in range(N)] for j in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visitChk[i][j] == 0:
                q = deque()
                q.append([i, j])
                opened = []
                sumpeople = 0
                visitChk[i][j] = 1
                while len(q) > 0:
                    if q[0][0] > 0:
                        if L <= abs(people[q[0][0] - 1][q[0][1]] - people[q[0][0]][q[0][1]]) <= R and visitChk[q[0][0] - 1][q[0][1]] == 0:
                            q.append([q[0][0] - 1, q[0][1]])
                            visitChk[q[0][0] - 1][q[0][1]] = 1
                    if q[0][1] > 0:
                        if L <= abs(people[q[0][0]][q[0][1] - 1] - people[q[0][0]][q[0][1]]) <= R and visitChk[q[0][0]][q[0][1] - 1] == 0:
                            q.append([q[0][0], q[0][1] - 1])
                            visitChk[q[0][0]][q[0][1] - 1] = 1
                    if q[0][0] < N - 1:
                        if L <= abs(people[q[0][0] + 1][q[0][1]] - people[q[0][0]][q[0][1]]) <= R and visitChk[q[0][0] + 1][q[0][1]] == 0:
                            q.append([q[0][0] + 1, q[0][1]])
                            visitChk[q[0][0] + 1][q[0][1]] = 1
                    if q[0][1] < N - 1:
                        if L <= abs(people[q[0][0]][q[0][1] + 1] - people[q[0][0]][q[0][1]]) <= R and visitChk[q[0][0]][q[0][1] + 1] == 0:
                            q.append([q[0][0], q[0][1] + 1])
                            visitChk[q[0][0]][q[0][1] + 1] = 1
                    opened.append(q[0])
                    sumpeople += people[q[0][0]][q[0][1]]
                    del q[0]
                lo = len(opened)
                if lo > 1:
                    flag = 1
                    afteropen = sumpeople // lo
                    for k in range(lo):
                        people[opened[k][0]][opened[k][1]] = afteropen
    if flag:
        return 1
    else:
        return 0

if __name__ == "__main__":
    main()
