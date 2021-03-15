import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    bus = []
    inf = 10000 * 6000 + 1
    disFrom0 = [inf for i in range(N)]
    disFrom0[0] = 0
    for i in range(M):
        s, e, t = map(int, sys.stdin.readline().split())
        bus.append([s - 1, e - 1, t])
    for i in range(1, N + 1):
        for j in range(M):
            s, e, t = bus[j][0], bus[j][1], bus[j][2]
            if disFrom0[s] != inf and disFrom0[s] + t < disFrom0[e]:
                disFrom0[e] = disFrom0[s] + t
                if i == N:
                    print(-1)
                    return
    for i in range(1, N):
        if disFrom0[i] == inf:
            print(-1)
        else:
            print(disFrom0[i])


if __name__ == '__main__':
    main()
