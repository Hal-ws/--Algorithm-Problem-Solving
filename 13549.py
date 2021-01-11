from queue import PriorityQueue


def main():
    N, K = map(int, input().split())
    visit = [0] * 200001
    q = PriorityQueue()
    q.put([0, N])
    visit[N] = 1
    while 1:
        a = q.get()
        t, p = a[0], a[1]
        if p == K:
            ans = t
            break
        if p * 2 <= 200000 and visit[p * 2] == 0:
            q.put([t, p * 2])
            visit[p * 2] = 1
        if p - 1 >= 0 and visit[p - 1] == 0:
            q.put([t + 1, p - 1])
            visit[p - 1] = 1
        if p + 1 <= 200000 and visit[p + 1] == 0:
            q.put([t + 1, p + 1])
            visit[p + 1] = 1
    print(ans)


if __name__ == '__main__':
    main()
