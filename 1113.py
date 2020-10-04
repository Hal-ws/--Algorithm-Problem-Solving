import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    pool = [0] * N
    for i in range(N):
        temp = list(sys.stdin.readline()[:M])
        for j in range(M):
            temp[j] = int(temp[j])
        pool[i] = temp
    print(pool)


def horizontal(i, j, pool):
    water = 0
    return water


def vertical(i, j, pool):
    water = 0
    return water

if __name__ == "__main__":
    main()
