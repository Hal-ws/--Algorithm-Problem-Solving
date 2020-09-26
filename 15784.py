import sys


def main():
    N, a, b = map(int, sys.stdin.readline().split())
    chairs = []
    flag = 0
    for i in range(N):
        chairs.append(list(map(int, sys.stdin.readline().split())))
    for i in range(N):
        if chairs[a - 1][i] > chairs[a - 1][b - 1]:
            flag = 1
            break
    for i in range(N):
        if flag:
            break
        if chairs[i][b - 1] > chairs[a - 1][b - 1]:
            flag = 1
            break
    if flag:
        print("ANGRY")
    else:
        print("HAPPY")


if __name__ == "__main__":
    main()
