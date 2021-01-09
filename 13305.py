import sys


def main():
    N = int(sys.stdin.readline())
    roads = list(map(int, sys.stdin.readline().split()))
    prices = list(map(int, sys.stdin.readline().split()))
    ans = 0
    pos = 0
    while pos < N - 1:
        prc = prices[pos]
        dis = 0
        for i in range(pos + 1, N):
            dis += roads[i - 1]
            if i != N - 1:
                iP = prices[i]
                if iP < prc:
                    nxt = i
                    ans += dis * prc
                    break
            else:
                nxt = i
                ans += dis * prc
        pos = nxt
    print(ans)


if __name__ == '__main__':
    main()
