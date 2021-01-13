import sys


def main():
    N = int(sys.stdin.readline())
    s = set()
    for i in range(N):
        a, b = map(str, sys.stdin.readline().split())
        if b == 'enter':
            s.add(a)
        else:
            s.remove(a)
    s = list(s)
    s.sort(reverse=True)
    for name in s:
        print(name)


if __name__ == '__main__':
    main()
