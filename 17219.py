import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    dic = {}
    for i in range(N):
        ad, pw = map(str, sys.stdin.readline().split())
        dic[ad] = pw
    for i in range(M):
        tmp = sys.stdin.readline()
        tmp = tmp[:len(tmp) - 1]
        print(dic[tmp])


if __name__ == '__main__':
    main()
