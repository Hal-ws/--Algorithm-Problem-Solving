import sys


def main():
    N = int(sys.stdin.readline())
    children = []
    ans = 0
    for i in range(N):
        children.append([int(sys.stdin.readline()), 0])
        if i == 0:
            children[i][1] = 1
        else:
            maxlen = 0
            for j in range(i - 1, -1, -1):
                if children[j][0] < children[i][0]:
                    if children[j][1] > maxlen:
                        maxlen = children[j][1]
            children[i][1] = maxlen + 1
        if children[i][1] > ans:
            ans = children[i][1]
    print(N - ans)


if __name__ == "__main__":
    main()
