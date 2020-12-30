import sys


def main():
    global relations, N, answer
    N, M = map(int, sys.stdin.readline().split())
    relations = [[] for i in range(N + 1)]  # i번 학생이 갖고 있는 친구의 목록
    visit = [0] * (N)
    answer = 0
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        relations[a].append(b)
        relations[b].append(a)
    for i in range(N):
        if answer:
            break
        visit[i] = 1
        dfs(i, 1, visit)
        visit[i] = 0
    print(answer)


def dfs(p, depth, visit):
    global relations, answer
    if depth == 5:
        answer = 1
    for nxt in relations[p]:
        if answer:
            break
        if visit[nxt] == 0:
            visit[nxt] = 1
            dfs(nxt, depth + 1, visit)
            visit[nxt] = 0


if __name__ == "__main__":
    main()
