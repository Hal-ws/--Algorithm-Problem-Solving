from queue import PriorityQueue
import sys


def main():
    N = int(sys.stdin.readline())
    que, cnt, answer = PriorityQueue(), 0, 0
    for i in range(N):
        que.put(int(sys.stdin.readline()))
        cnt += 1
    if cnt == 1:
        print(0)
    else:
        for i in range(cnt - 1):
            first = que.get()
            second = que.get()
            answer += (first + second)
            que.put(first + second)
        print(answer)

if __name__ == "__main__":
    main()
