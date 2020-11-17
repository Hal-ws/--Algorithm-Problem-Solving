import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    miro = []
    ans = 0
    for i in range(N):
        miro.append(sys.stdin.readline()[:M])
    chk = [[0 for i in range(M)] for j in range(N)] ## 0: 아직 확인안함. 1: 탈출가능, -1: 탈출불가능
    for i in range(N):
        for j in range(M):
            if chk[i][j] == 0:
                ans += chkescape(miro, chk, [i, j], N, M)
    print(ans)


def chkescape(miro, chk, pos, N, M):
    path = [pos]
    idx, flag = 0, 1 ## flag: -1 -> 불가능. path에 있던 좌표들 전부다 chk에 -1 입력. flag=: 1. 가능.
    while 1:
        if chk[path[idx][0]][path[idx][1]] == -1 or chk[path[idx][0]][path[idx][1]] == 2: ## chk값이 2: 이미 방문한점 다시 방문했다는 뜻
            flag = -1
            idx -= 1
            break
        if chk[path[idx][0]][path[idx][1]] == 1:
            idx -= 1
            break
        if miro[path[idx][0]][path[idx][1]] == "U":
            if path[idx][0] == 0:
                break
            chk[path[idx][0]][path[idx][1]] = 2
            path.append([path[idx][0] - 1, path[idx][1]])
        if miro[path[idx][0]][path[idx][1]] == "D":
            if path[idx][0] == N - 1:
                break
            chk[path[idx][0]][path[idx][1]] = 2
            path.append([path[idx][0] + 1, path[idx][1]])
        if miro[path[idx][0]][path[idx][1]] == "L":
            if path[idx][1] == 0:
                break
            chk[path[idx][0]][path[idx][1]] = 2
            path.append([path[idx][0], path[idx][1] - 1])
        if miro[path[idx][0]][path[idx][1]] == "R":
            if path[idx][1] == M - 1:
                break
            chk[path[idx][0]][path[idx][1]] = 2
            path.append([path[idx][0], path[idx][1] + 1])
        idx += 1
    if flag == -1:
        for i in range(idx + 1):
            chk[path[i][0]][path[i][1]] = -1
        return 0
    if flag == 1:
        for i in range(idx + 1):
            chk[path[i][0]][path[i][1]] = 1
        return idx + 1


if __name__ == "__main__":
    main()
