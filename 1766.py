import sys
import heapq


def main():
    N, M = map(int, sys.stdin.readline().split())
    heap = []
    connect = [[] for i in range(N + 1)]
    inDegree = [0 for i in range(N + 1)]
    answer = []
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        connect[a].append(b)
        inDegree[b] += 1
    for i in range(1, N + 1):
        if inDegree[i] == 0:
            heapq.heappush(heap, i)
    while len(heap) > 0:
        cur = heapq.heappop(heap)
        answer.append(cur)
        for nxt in connect[cur]:
            inDegree[nxt] -= 1
            if inDegree[nxt] == 0:
                heapq.heappush(heap, nxt)
    for i in range(N):
        print(answer[i], end=' ')


if __name__ == '__main__':
    main()
