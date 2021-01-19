import sys


def main():
    N = int(sys.stdin.readline())
    building, stack = [], []
    ans = [-1] * N
    for i in range(N):
        building.append(int(sys.stdin.readline()))
    ans[N - 1] = 0
    stack.append([building[N - 1], 0])
    for i in range(N - 2, -1, -1):
        height = building[i]
        watch = 0
        while len(stack) > 0:
            tmp = stack.pop()
            tmpH = tmp[0]
            if height > tmpH:
                watch += (1 + tmp[1])
            else:
                stack.append(tmp)
                break
        stack.append([height, watch])
        ans[i] = watch
    print(sum(ans))


if __name__ == '__main__':
    main()
