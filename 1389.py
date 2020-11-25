import sys
from _collections import deque


def main():
    N, M = map(int, sys.stdin.readline().split())
    relations = [[0 for i in range(N + 1)] for j in range(N + 1)]
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        relations[a][b] = 1
        relations[b][a] = 1
    people = [[0, i] for i in range(N + 1)]
    for i in range(1, N + 1):
        people[i][0] = kevinnum(relations, i, N)
    minNum = 9999999999999999999
    ans = 0
    for i in range(1, N + 1):
        if people[i][0] < minNum:
            minNum = people[i][0]
            ans = people[i][1]
    print(ans)


def kevinnum(relations, a, N): #a의 케빈 베이컨의 수를 구한다
    chk = [-1] * (N + 1) #몇단계인지 표시
    chk[a] = 0 #자기자신은 0단계
    q = deque()
    q.append(a)
    while len(q) > 0:
        cur = q[0] #현재 학생
        for i in range(N + 1):
            if relations[cur][i] == 1 and chk[i] == -1: # cur과 i가 친구인데 아직 방문안했음
                q.append(i)
                chk[i] = chk[q[0]] + 1
        q.popleft()
    result = 0
    for i in range(N + 1):
        if chk[i] != -1:
            result += chk[i]
    return result


if __name__ == "__main__":
    main()
