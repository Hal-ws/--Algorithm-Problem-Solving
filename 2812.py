import sys


def main():
    N, K = map(int, sys.stdin.readline().split())
    num = sys.stdin.readline()[:N]
    stack = []
    stack.append(num[0])
    dCnt = 0
    for i in range(1, N):
        if dCnt < K:
            while 1:
                if stack[-1] < num[i]: # 더 큰값을 넣을때
                    stack.pop()
                    dCnt += 1
                else:
                    break
                if dCnt == K or len(stack) == 0:
                    break
        stack.append(num[i])
    for i in range(dCnt, K):
        stack.pop()
    for i in range(N - K):
        print(stack[i], end='')


if __name__ == '__main__':
    main()
