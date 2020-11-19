import sys
from collections import deque


def main():
    R, C = map(int, sys.stdin.readline().split())
    cave = []
    for i in range(R):
        cave.append(list(sys.stdin.readline()[:C]))
    N = int(sys.stdin.readline)
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
                pos = [R -height][j]
                break
    else:
        for j in range(C - 1, -1, -1):
            if cave[R - height][j] == "x":
                cave[R - height][j] = "."
                pos = [R - height][j]
                break
    ## 부수는 작업 끝. 부숴진것 때문에 두개로 갈라졌는지 확인.
    bfs(cave, R, C) #바닥에 붙어있는 클러스터 / 떨어져있는 클러스터로 구분


def bfs(cave, R, C):
    chk = [[0 for i in range(C)] for j in range(R)]

    return 0


if __name__ == "__main__":
    main()
