import sys
from queue import PriorityQueue
def main():
    N = int(sys.stdin.readline())
    que = PriorityQueue()
    cnt = 0
    for i in range(N):
        query = int(sys.stdin.readline())
        if query == 0:
            if cnt == 0:
                print(0)
            else:
                output = que.get()
                print(output * (-1))
                cnt -= 1
        else:
            que.put(query * (-1))
            cnt += 1

if __name__ == "__main__":
    main()
