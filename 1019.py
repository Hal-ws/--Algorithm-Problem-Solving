import sys

N = int(sys.stdin.readline())

def getdegree(N):
    return len(str(N)) - 1

def cntn(N, val):
    if N < 10:
        if N >= val:
            return 1
        return 0
    else:
        degree = getdegree(N)
        first = N // pow(10, degree)
        if first == val:
            return cntn(first * pow(10, degree) - 1, val) + (N - first * pow(10, degree) + 1) + cntn(N - first * pow(10, degree), val)
        else:
            return cntn(first * pow(10, degree) - 1, val) + cntn(N - first * pow(10, degree), val)
ans = []
for i in range(10):
    ans.append(cntn(N, i))
    print(ans[i], end=' ')
