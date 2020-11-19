import sys
from collections import deque


def main():
    R, C = map(int, sys.stdin.readline().split())
    cave = []
    for i in range(R):
        cave.append(list(sys.stdin.readline()[:C]))
    N = int(sys.stdin.readline())
    throws = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        throwing(cave, throws[i], i, R, C)
    for i in range(R):
        for j in range(C):
            print(cave[i][j], end='')
        print()


def throwing(cave, height, direction, R, C): #i 가 짝수: 왼쪽에서 오른쪽. i가 홀수: 오른쪽에서 왼쪽
    if direction % 2 == 0:
        for j in range(C):
            if cave[R - height][j] == "x":
                cave[R - height][j] = "."
                break
    else:
        for j in range(C - 1, -1, -1):
            if cave[R - height][j] == "x":
                cave[R - height][j] = "."
                break
    ## 바닥이랑 연결된 클러스터 확인
    chk = [[0 for i in range(C)] for j in range(R)]
    cnt = 1
    q = deque()
    for i in range(C):
        if chk[R - 1][i] == 0 and cave[R - 1][i] == "x":
            q.append([R - 1, i])
            bfs(cave, chk, q, cnt, R, C) # 바닥과 연결된 클러스터를 다 1로 체크
    endflag = 0
    for i in range(R): # 떨어지는 cluster 찾음
        for j in range(C):
            if cave[i][j] == "x" and chk[i][j] != 1:
                cnt += 1
                q.append([i, j])
                bfs(cave, chk, q, cnt, R, C)
                endflag = 1
                break
        if endflag:
            break
    ## 이제 seperated cluster를 떨어트림
    boundary = []
    for i in range(C):
        for j in range(R - 1, -1, -1):
            if chk[j][i] == 2:
                boundary.append([j, i])
                break
    distance = 0  #떨어지는 길이 설정
    lb = len(boundary)
    endflag = 0
    if lb > 0:
        while 1:
            distance += 1
            for i in range(lb):
                boundary[i][0] += 1
                if boundary[i][0] == R or chk[boundary[i][0]][boundary[i][1]] == 1:
                    endflag = 1
                    distance -= 1
                    break
            if endflag:
                break
        for j in range(C):
            for i in range(R - 1, -1, -1):
                if chk[i][j] == 2:
                    cave[i][j] = "."
                    cave[i + distance][j] = "x"


def bfs(cave, chk, q, cnt, R, C):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    chk[q[0][0]][q[0][1]] = cnt
    while len(q) > 0:
        for i in range(4):
            if 0 <= q[0][0] + dy[i] < R and 0 <= q[0][1] + dx[i] < C:
                if cave[q[0][0] + dy[i]][q[0][1] + dx[i]] == 'x' and chk[q[0][0] + dy[i]][q[0][1] + dx[i]] == 0:
                    q.append([q[0][0] + dy[i], q[0][1] + dx[i]])
                    chk[q[0][0] + dy[i]][q[0][1] + dx[i]] = cnt
        q.popleft()


if __name__ == "__main__":
    main()
