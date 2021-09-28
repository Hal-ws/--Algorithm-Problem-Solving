import sys


def main():
    N = int(sys.stdin.readline())
    start = list(map(int, sys.stdin.readline()[:N]))
    target = list(map(int, sys.stdin.readline()[:N]))
    val1 = changing(0, start, target, N)
    val2 = changing(1, start, target, N)
    if min(val1, val2) == 100001:
        print(-1)
    else:
        print(min(val1, val2))


def changing(sIdx, start, target, N):
    diffChk = [0] * N
    cnt = 0
    for i in range(N):
        if start[i] != target[i]:
            diffChk[i] = 1
        else:
            diffChk[i] = 0
    if sIdx == 0:
        diffChk[0] = (diffChk[0] + 1) % 2
        diffChk[1] = (diffChk[1] + 1) % 2
        cnt = 1
    for i in range(1, N):
        if i - 1 >= 0:
            if diffChk[i - 1]:
                cnt += 1
                diffChk[i - 1] = 0
                diffChk[i] = (diffChk[i] + 1) % 2
                if i + 1 < N:
                    diffChk[i + 1] = (diffChk[i + 1] + 1) % 2
    for i in range(N):
        if diffChk[i]:
            return 100001
    return cnt


if __name__ == "__main__":
    main()
