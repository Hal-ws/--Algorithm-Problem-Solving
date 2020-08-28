import sys

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        M, N, K = map(int, sys.stdin.readline().split())
        field = [[0 for j in range(M)] for k in range(N)]
        setbugs(K, field)
        print(bfs(field, N, M))
def bfs(field, N, M):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                cnt += 1
                queue = []
                extend(field, i, j, queue)
                while len(queue) > 0:
                    extend(field, queue[0][0], queue[0][1], queue)
                    del queue[0]
    return cnt

def extend(field, i, j, queue):
    N = len(field)
    M = len(field[0])
    if i > 0 and field[i - 1][j] == 1: ## 위로 이동
        addqueue(field, i - 1, j, queue)
    if i < N - 1 and field[i + 1][j] == 1: ## 아래로 이동
        addqueue(field, i + 1, j, queue)
    if j > 0 and field[i][j - 1] == 1: ## 왼쪽으로 이동
        addqueue(field, i, j - 1, queue)
    if j < M - 1 and field[i][j + 1] == 1:
        addqueue(field, i, j + 1, queue)

def addqueue(field, i, j, queue):
    queue.append([i, j]) ## 위치를 저장
    field[i][j] = 2 ## queue에 더해지면 2로 변경한다

def setbugs(K, field):
    for k in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        field[Y][X] = 1

if __name__ == "__main__":
    main()
