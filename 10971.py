import sys


def main():
    N = int(sys.stdin.readline())
    board = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    minVal = [100000001]
    for i in range(N):
        visited = [0] * N
        visited[i] = 0
        dfs(i, N, board, visited, 1, i, 0, minVal)
    print(minVal[0])


def dfs(start, N, board, visited, level, cur, price, minVal): #cur: 지금 있는 도시 index. level: cur을 포함해서 방문한 도시의 수
    if level == N: # 끝까지 다 돌았을때 시작점으로 돌아가는지 확인한다
        if visited[start] == 0 and board[cur][start] != 0:
            result = price + board[cur][start]
            if result < minVal[0]:
                minVal[0] = result
        return
    for i in range(N):
        if i == start:
            continue
        if visited[i] == 0 and board[cur][i] != 0: # 방문 안한 도시 확인
            add = board[cur][i] # cur 도시에서 i 도시로 가는 비용
            visited[i] = 1
            dfs(start, N, board, visited, level + 1, i, price + add, minVal)
            visited[i] = 0


if __name__ == "__main__":
    main()
