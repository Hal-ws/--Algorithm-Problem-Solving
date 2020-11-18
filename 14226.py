from collections import deque


def main():
    S = int(input())
    chk = [[-1 for i in range(2001)] for j in range(2001)] #도착시간 걸어둠
    chk[1][0] = 0
    chk[2][1] = 2
    q = deque()
    q.append([1, 0, 0]) # 개수, 클립보드 저장된 양, 시간
    q.append([2, 1, 2])
    while len(q) > 0:
        if q[0][0] * 2 <= 2000: # 2배 곱함
            if chk[q[0][0] * 2][q[0][0]] == - 1 or chk[q[0][0] * 2][q[0][0]] > q[0][2] + 2:
                chk[q[0][0] * 2][q[0][0]] = q[0][2] + 2
                q.append([q[0][0] * 2, q[0][0], q[0][2] + 2])
        if q[0][0] + q[0][1] <= 2000: # 지금 클립보드에 저장된값 더함
            if chk[q[0][0] + q[0][1]][q[0][1]] == -1 or chk[q[0][0] + q[0][1]][q[0][1]] > q[0][2] + 1:
                chk[q[0][0] + q[0][1]][q[0][1]] = q[0][2] + 1
                q.append([q[0][0] + q[0][1], q[0][1], q[0][2] + 1])
        if q[0][0] - 1 >= 0:
            if chk[q[0][0] - 1][q[0][1]] == -1 or chk[q[0][0] - 1][q[0][1]] > q[0][2] + 1:
                chk[q[0][0] - 1][q[0][1]] = q[0][2] + 1
                q.append([q[0][0] - 1, q[0][1], q[0][2] + 1])
        q.popleft()
    ans = 9999999999999999999
    for i in range(2000):
        if chk[S][i] != -1 and chk[S][i] <= ans:
            ans = chk[S][i]
    print(ans)


if __name__ == "__main__":
    main()
