import sys
from _collections import deque


def main():
    global h, w, minK
    T = int(sys.stdin.readline())
    for _ in range(T):
        h, w = map(int, sys.stdin.readline().split())
        board = [['.'] * (w + 2)]
        p = []
        for i in range(h):
            board.append(['.'] + list(sys.stdin.readline()[:w]) + ['.'])
            for j in range(w + 2):
                if board[i + 1][j] == '$':
                    p.append([i + 1, j])
        p.append([0, 0])
        board.append(['.'] * (w + 2))
        # 최소 열쇠 수를 p1, p2, 외부인 이렇게 각각 저장
        minK = [[[-1 for j in range(w + 2)] for i in range(h + 2)] for k in range(3)]
        for i in range(3):
            bfs(p[i], i)

def bfs(p, idx):
    global h, w, minK
    q = deque()
    visit = [[0 for j in range(w + 2)] for i in range(h + 2)]
    kList = minK[idx]
    q.append([p[0], p[1], 0]) # y, x, 가진 키

    return 0


if __name__ == '__main__':
    main()
