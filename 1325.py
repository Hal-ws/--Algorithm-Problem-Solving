import sys
from collections import deque


def main():
    global N
    N, M = map(int, sys.stdin.readline().split())
    trust = [[] for i in range(N + 1)] # i번 컴퓨터를 신뢰하는 컴퓨터들
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split()) #a가 b를 신뢰함
        trust[b].append(a)
    answer = [0] * (N + 1)
    answer[0] = [0, 0]
    for i in range(1, N + 1):
        answer[i] = [bfs(trust, i), -i]
    answer.sort(reverse=True)
    maxCnt = answer[0][0]
    for ans in answer:
        if ans[0] == maxCnt:
            print(-1 * ans[1], end=' ')


def bfs(trust, computer): #i번(computer)로 해킹할 수 있는 컴퓨터 조사
    global N
    visitChk = [0] * (N + 1)
    q = deque()
    q.append(computer)
    visitChk[computer] = 1
    cnt = 0
    while len(q) > 0:
        cur = q[0]
        for nxt in trust[cur]:
            if visitChk[nxt] == 0:
                q.append(nxt)
                visitChk[nxt] = 1
                cnt += 1
        q.popleft()
    return cnt


if __name__ == "__main__":
    main()
