import sys
from _collections import deque


def main():
    N, K = map(int, sys.stdin.readline().split())
    brotherT = [-1] * 500001 # 동생이 idx 에 도착할때까지 걸린 시간 기록
    subinOdd = [-1] * 500001
    subinEven = [-1] * 500001
    flag = 0
    ans = 500001
    t = 0
    while 1:
        p = K + (t * (t + 1) // 2)
        if p > 500000:
            break
        brotherT[p] = t
        t += 1
    bfs(N, subinOdd, subinEven)
    for i in range(500001):
        tmpT = brotherT[i]
        if tmpT != -1:
            if tmpT % 2 == 0: # 동생이 짝수에 도착
                if subinEven[i] == tmpT:
                    flag = 1
                    if tmpT < ans:
                        ans = tmpT
                if subinEven[i] < tmpT and (tmpT - subinEven[i]) % 2 == 0:
                    flag = 1
                    if tmpT < ans:
                        ans = tmpT
            if tmpT % 2 == 1:
                if subinOdd[i] == tmpT:
                    flag = 1
                    if tmpT < ans:
                        ans = tmpT
                if subinOdd[i] < tmpT and (tmpT - subinOdd[i]) % 2 == 0:
                    flag = 1
                    if tmpT < ans:
                        ans = tmpT
    if flag:
        print(ans)
    else:
        print(-1)


def bfs(N, subinOdd, subinEven):
    q = deque()
    q.append([N, 0])
    subinEven[N] = 0
    while len(q) > 0:
        p = q[0][0]
        t = q[0][1]
        if t % 2 == 0:
            flag = 1
        else:
            flag = 0
        if 0 <= p - 1 :
            if flag:
                if subinOdd[p - 1] == -1:
                    subinOdd[p - 1] = t + 1
                    q.append([p - 1, t + 1])
            else:
                if subinEven[p - 1] == -1:
                    subinEven[p - 1] = t + 1
                    q.append([p - 1, t + 1])
        if p + 1 <= 500000:
            if flag:
                if subinOdd[p + 1] == -1:
                    subinOdd[p + 1] = t + 1
                    q.append([p + 1, t + 1])
            else:
                if subinEven[p + 1] == -1:
                    subinEven[p + 1] = t + 1
                    q.append([p + 1, t + 1])
        if p * 2 <= 500000:
            if flag:
                if subinOdd[p * 2] == -1:
                    subinOdd[p * 2] = t + 1
                    q.append([p * 2, t + 1])
            else:
                if subinEven[p * 2] == -1:
                    subinEven[p * 2] = t + 1
                    q.append([p * 2, t + 1])
        q.popleft()


if __name__ == '__main__':
    main()
