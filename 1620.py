import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    nameBook =[0] * (N + 1)
    numBook = {}
    for i in range(N):
        name = sys.stdin.readline().rstrip()
        nameBook[i + 1] = name
        numBook[name] = i + 1
    for i in range(M):
        a = sys.stdin.readline().rstrip()
        if ord(a[0]) >= 65: #문자를 입력받음
            print(numBook[a])
        else:
            a = int(a)
            print(nameBook[a])


if __name__ == '__main__':
    main()
