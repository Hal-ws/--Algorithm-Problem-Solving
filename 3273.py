import sys


def main():
    n = int(sys.stdin.readline())
    nList = list(map(int, sys.stdin.readline().split()))
    x = int(sys.stdin.readline())
    nList.sort()
    s, e = 0, n - 1
    cnt = 0
    while s < e:
        val = nList[s] + nList[e]
        if val == x:
            cnt += 1
            s += 1
        elif val > x:
            e -= 1
        else:
            s += 1
    print(cnt)


if __name__ == '__main__':
    main()
