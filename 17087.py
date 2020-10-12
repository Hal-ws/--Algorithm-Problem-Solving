from math import gcd


def main():
    N, S = map(int, input().split())
    dis = list(map(int, input().split()))
    for i in range(N):
        dis[i] = abs(S - dis[i])
    if N == 1:
        print(dis[0])
    else:
        gcdlist= [gcd(dis[0], dis[1])]
        for i in range(1, N - 1):
            gcdlist.append(gcd(gcdlist[i - 1], dis[i + 1]))
        print(gcdlist[N - 2])


if __name__ == '__main__':
    main()
