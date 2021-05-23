import sys


def main():
    N = int(sys.stdin.readline())
    l1, l2 = [], []
    cnt = 0
    for i in range(N):
        l1.append(sys.stdin.readline())
    for i in range(N):
        l2.append(sys.stdin.readline())
    while len(l1) > 0:
        if l1[-1] == l2[-1]:
            l1.pop()
            l2.pop()
        else:
            delIdx = l2.index(l1[-1])
            cnt += 1
            l1.pop()
            del l2[delIdx]
    print(cnt)


if __name__ == '__main__':
    main()
