import sys
from collections import deque


def main():
    N, M, K = map(int, sys.stdin.readline().split())
    A, trees, deadtrees = [], deque(), deque()
    field = [[5 for i in range(N)] for j in range(N)]
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    #A: 매 겨울마다 밭에 더해지는 양분 field: 현재 밭의 양분 상태. trees: 지금 밭에 있는 나무, deadtrees: 죽은 나무
    for i in range(N):
        A.append(list(map(int, sys.stdin.readline().split())))
        field.append(A[i])
    for i in range(M):
        temp = list(map(int, sys.stdin.readline().split()))
        trees.append([N - temp[1], temp[0] - 1, temp[2]])
    lt = len(trees)
    for i in range(K):
        lt = spring(trees, deadtrees, field, lt)
        summer(deadtrees, field)
        lt = fall(trees, dx, dy, lt, N)
        winter(A, field, N)
    print(lt)


def spring(trees, deadtrees, field, lt):
    for i in range(lt):
        if trees[0][2] > field[trees[0][0]][trees[0][1]]: #트리가 죽음
            deadtrees.append(trees.popleft())
            lt -= 1
        else:
            field[trees[0][0]][trees[0][1]] -= trees[0][2]
            trees[0][2] += 1
            trees.append(trees.popleft())
    return lt


def summer(deadtrees, field):
    ld = len(deadtrees)
    for i in range(ld):
        temp = deadtrees.popleft()
        field[temp[0]][temp[1]] += (temp[2] // 2)


def fall(trees, dx, dy, lt, N):
    adding = 0
    for i in range(lt):
        if trees[i + adding][2] % 5 == 0:
            for j in range(8):
                x = trees[i + adding][1] + dx[j]
                y = trees[i + adding][0] + dy[j]
                if 0 <= x < N and 0 <= y < N:
                    trees.appendleft([y, x, 1])
                    adding += 1
                    lt += 1
    return lt


def winter(A, field, N):
    for i in range(N):
        for j in range(N):
            field[i][j] += A[i][j]


if __name__ == "__main__":
    main()
