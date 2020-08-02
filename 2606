def main():
    N = int(input())
    connections = int(input())
    matrix = [[0 for i in range(N)] for j in range(N)]
    for i in range(connections):
        x, y = map(int, input().split())
        matrix[x - 1][y - 1] = 1
        matrix[y - 1][x - 1] = 1
    print(bfs(matrix, 1))


def bfs(matrix, start):
    queue = []
    N = len(matrix)
    infected = 0
    visitchk = [1] + [0] * (N - 1) ## 방문한 컴퓨터는 1,로 표시, 방문 안한 컴퓨터는 0 표시
    for i in range(N):
        if matrix[0][i] == 1:
            queue.append(i + 1) ## 1번 컴퓨터랑 연결된 컴퓨터를 queue에 추가
            visitchk[i] = 1
            infected += 1
    while len(queue) > 0: ## queue에 저장된 숫자: n번 컴퓨터(1부터 시작)
        for i in range(N):
            if matrix[queue[0] - 1][i] == 1 and visitchk[i] == 0:
                queue.append(i + 1)
                visitchk[i] = 1
                infected += 1
        del queue[0]
    return infected

if __name__ == "__main__":
    main()
