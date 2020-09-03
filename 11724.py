from collections import deque
import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    matrix, visitChk = [[0 for i in range(N)] for j in range(N)], [0] * N
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        matrix[a - 1][b - 1] = 1
        matrix[b - 1][a - 1] = 1
    answer = 0
    for i in range(N):
        if visitChk[i] == 0:
            visitChk[i] = 1
            answer += 1
            q = deque([i])
            while len(q) > 0:
                for j in range(N):
                    if visitChk[j] == 0 and matrix[q[0]][j] == 1:
                        visitChk[j] = 1
                        q.append(j)
                q.popleft()

    print(answer)
    return 0


if __name__ == "__main__":
    main()
