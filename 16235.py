import sys
from collections import deque


def main():
    N, M, K = map(int, sys.stdin.readline().split())
    A, trees, deadtrees = [], deque(), deque()
    field = [[5 for i in range(N)] for j in range(N)]
    #A: 매 겨울마다 밭에 더해지는 양분 field: 현재 밭의 양분 상태. trees: 지금 밭에 있는 나무, deadtrees: 죽은 나무
    for i in range(N):
        A.append(list(map(int, sys.stdin.readline().split())))
        field.append(A[i])
    for i in range(M):
        temp = list(map(int, sys.stdin.readline().split()))
        trees.append([N - temp[1], temp[0] - 1, temp[2]])
    for i in range(K):
        spring(trees, deadtrees, field)
        summer(deadtrees, field)
        fall(trees, N)
        winter(A, field, N)

    print(len(trees))


def spring(trees, deadtrees, field):
    lt = len(trees)
    for i in range(lt):
        if trees[0][2] > field[trees[0][0]][trees[0][1]]: #트리가 죽음
            deadtrees.append(trees.popleft())
        else:
            field[trees[0][0]][trees[0][1]] -= trees[0][2]
            trees[0][2] += 1
            trees.append(trees.popleft())


def summer(deadtrees, field):
    ld = len(deadtrees)
    for i in range(ld):
        temp = deadtrees.popleft()
        field[temp[0]][temp[1]] += (temp[2] // 2)


def fall(trees, N):
    lt = len(trees)
    adding = 0
    for i in range(lt):
        if trees[i + adding][2] % 5 == 0:
            if trees[i + adding][0] > 0:
                trees.appendleft([trees[i + adding][0] - 1, trees[i + adding][1], 1])
                adding += 1
                if trees[i + adding][1] > 0:
                    trees.appendleft([trees[i + adding][0] - 1, trees[i + adding][1] - 1, 1])
                    adding += 1
                if trees[i + adding][1] < N - 1:
                    trees.appendleft([trees[i + adding][0] - 1, trees[i + adding][1] + 1, 1])
                    adding += 1
            if trees[i + adding][0] < N - 1:
                trees.appendleft([trees[i + adding][0] + 1, trees[i + adding][1], 1])
                adding += 1
                if trees[i + adding][1] > 0:
                    trees.appendleft([trees[i + adding][0] + 1, trees[i + adding][1] - 1, 1])
                    adding += 1
                if trees[i + adding][1] < N - 1:
                    trees.appendleft([trees[i + adding][0] + 1, trees[i + adding][1] + 1, 1])
                    adding += 1
            if trees[i + adding][1] > 0:
                trees.appendleft([trees[i + adding][0], trees[i + adding][1] - 1, 1])
                adding += 1
            if trees[i + adding][1] < N - 1:
                trees.appendleft([trees[i + adding][0], trees[i + adding][1] + 1, 1])
                adding += 1


def winter(A, field, N):
    for i in range(N):
        for j in range(N):
            field[i][j] += A[i][j]


if __name__ == "__main__":
    main()
