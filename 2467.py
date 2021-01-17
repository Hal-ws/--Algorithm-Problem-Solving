import sys


def main():
    N = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    s, e = 0, N - 1
    minV = 2000000001
    ans = [0, 0]
    l.sort()
    while s < e:
        tmp = l[s] + l[e]
        uflag, dflag = 0, 0
        if tmp == 0:
            ans[0] = l[s]
            ans[1] = l[e]
            break
        elif tmp > 0:
            e -= 1
            dflag = 1
        else:
            s += 1
            uflag = 1
        if abs(tmp) < minV:
            minV = abs(tmp)
            if uflag:
                ans[0] = l[s - 1]
                ans[1] = l[e]
            if dflag:
                ans[0] = l[s]
                ans[1] = l[e + 1]
    print('%s %s' %(ans[0], ans[1]))


if __name__ == '__main__':
    main()

