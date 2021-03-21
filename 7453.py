import sys


def main():
    N = int(sys.stdin.readline())
    A, B, C, D = [0] * N, [0] * N, [0] * N, [0] * N
    ans = 0
    for i in range(N):
        ta, tb, tc, td = map(int, sys.stdin.readline().split())
        A[i], B[i], C[i], D[i] = ta, tb, tc, td
    AB, CD = [], {}
    for i in range(N):
        for j in range(N):
            AB.append(A[i] + B[j])
            if CD.get(C[i] + D[j]) == None:
                CD[C[i] + D[j]] = 1
            else:
                CD[C[i] + D[j]] += 1
    for num in AB:
        if CD.get(-num) != None:
            ans += CD.get(-num)
    print(ans)


if __name__ == '__main__':
    main()
