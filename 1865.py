import sys


def main():
    TC = int(sys.stdin.readline())
    inf = 22 * pow(10, 8)
    for _ in range(TC):
        N, M, W = map(int, sys.stdin.readline().split())
        ans = 'NO'
        dFrom1 = [inf] * (N + 1)
        dFrom1[1] = 0
        edges = []
        for i in range(M):
            s1, s2, d = map(int, sys.stdin.readline().split())
            edges.append([s1, s2, d])
            edges.append([s2, s1, d])
        for i in range(W):
            s, e, d = map(int, sys.stdin.readline().split())
            edges.append([s, e, -1 * d])
        for i in range(1, N + 1):
            for j in range(2 * M + W):
                s, e, d = edges[j][0], edges[j][1], edges[j][2]
                if s != inf and dFrom1[s] + d < dFrom1[e]:
                    dFrom1[e] = dFrom1[s] + d
                    if i == N:
                        ans = 'YES'
                        break
            if ans == 'YES':
                break
        print(ans)


if __name__ == '__main__':
    main()
