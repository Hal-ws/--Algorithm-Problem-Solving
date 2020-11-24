from collections import deque


def main():
    stones = list(map(int, input().split()))
    stones.sort()
    visitChk = [[0 for i in range(1001)] for j in range(1001)]
    q = deque()
    q.append(stones)
    visitChk[stones[0]][stones[1]] = 1
    print(bfs(q, visitChk))


def bfs(q, visitchk):
    while len(q) > 0:
        temp = [0, 0, q[0][2]] # 0, 1번
        process(q, visitchk, temp, 0, 1)
        temp = [0, q[0][1], 0]  # 0, 2번
        process(q, visitchk, temp, 0, 2)
        temp = [q[0][0], 0, 0]  # 1, 2번
        process(q, visitchk, temp, 1, 2)
        if q[0][0] == q[0][1] == q[0][2]:
            return 1
        q.popleft()
    return 0


def process(q, visitChk, temp, i, j):
    temp[i] = q[0][i] + q[0][i]
    temp[j] = q[0][j] - q[0][i]
    temp.sort()
    print('temp: %s' %temp)
    if visitChk[temp[0]][temp[1]] == 0:
        q.append(temp)
        visitChk[temp[0]][temp[1]] = 1


if __name__ == "__main__":
    main()
