import sys


def cntCutted(lines, length):
    l = len(lines)
    cnt = 0
    for i in range(l):
        cnt += lines[i] // length
    return cnt

def main():
    K, N =map(int, sys.stdin.readline().split())
    lines = [0] * K
    for i in range(K):
        lines[i] = int(sys.stdin.readline())
    minLen = 0
    maxLen = max(lines)
    while minLen <= maxLen:
        midLen = (minLen + maxLen) // 2
        if midLen == 0:
            midLen = 1
        cnt = cntCutted(lines, midLen)
        if cnt >= N:
            minLen = midLen + 1
        else:
            maxLen = midLen - 1
    print(maxLen)

if __name__ == "__main__":
    main()
