import sys


def main():
    N1, N2 = map(int, sys.stdin.readline().split())
    gr1 = list(sys.stdin.readline()[:N1])
    gr2 = list(sys.stdin.readline()[:N2])
    T = int(sys.stdin.readline())
    gr1 = list(reversed(gr1))
    v = [1] * N1 + [-1] * N2
    gr = gr1 + gr2
    for i in range(T):
        j = 0
        while j < N1 + N2 - 1:
            if v[j] == 1 and v[j] != v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                gr[j], gr[j + 1] = gr[j + 1], gr[j]
                j += 2
            else:
                j += 1
    for i in range(N1 + N2):
        print(gr[i], end='')


if __name__ == '__main__':
    main()
