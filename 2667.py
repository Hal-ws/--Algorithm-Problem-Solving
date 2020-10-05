import sys

def main():
    N = int(sys.stdin.readline())
    apartment = []
    for i in range(N):
        apartment.append(sys.stdin.readline())
    ans = sorted(bfs(apartment))
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i])


def bfs(apartment):
    l = len(apartment)
    visitchk = [[0 for i in range(l)] for j in range(l)] ## 0 이면 방문 안한것
    ans = []
    for i in range(l):
        for j in range(l):
            if apartment[i][j] == '1' and visitchk[i][j] == 0:
                q = []
                q.append([i, j])
                visitchk[i][j] = 1
                cnt = 1
                while len(q) > 0:
                    if q[0][0] > 0 and apartment[q[0][0] - 1][q[0][1]] == '1' and visitchk[q[0][0] - 1][q[0][1]] == 0:
                        q.append([q[0][0] - 1, q[0][1]])
                        visitchk[q[0][0] - 1][q[0][1]] = 1
                        cnt += 1
                    if q[0][1] < l - 1 and apartment[q[0][0]][q[0][1] + 1] == '1' and visitchk[q[0][0]][q[0][1] + 1] == 0:
                        q.append([q[0][0], q[0][1] + 1])
                        visitchk[q[0][0]][q[0][1] + 1] = 1
                        cnt += 1
                    if q[0][0] < l - 1 and apartment[q[0][0] + 1][q[0][1]] == '1' and visitchk[q[0][0] + 1][q[0][1]] == 0:
                        q.append([q[0][0] + 1, q[0][1]])
                        visitchk[q[0][0] + 1][q[0][1]] = 1
                        cnt += 1
                    if q[0][1] > 0 and apartment[q[0][0]][q[0][1] - 1] == '1' and visitchk[q[0][0]][q[0][1] - 1] == 0:
                        q.append([q[0][0], q[0][1] - 1])
                        visitchk[q[0][0]][q[0][1] - 1] = 1
                        cnt += 1
                    del q[0]
                ans.append(cnt)
    return ans


if __name__ == "__main__":
    main()
