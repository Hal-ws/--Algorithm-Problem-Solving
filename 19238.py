import sys
from collections import deque


def main():
    N, M, F = map(int, sys.stdin.readline().split())
    board, arrive = [], [[None, None]]
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    taxi = list(map(int, sys.stdin.readline().split()))
    taxi[0], taxi[1] = taxi[0] - 1, taxi[1] - 1
    for i in range(M):
        y, x, ay, ax = map(int, sys.stdin.readline().split())
        board[y - 1][x - 1] = -1 * (i + 1)
        arrive.append([ay - 1, ax - 1])
    while 1:
        tmp = getnearcustomer(board, taxi, N)
        if tmp == -1: #태워줄 수 있는 손님이 없음
            for i in range(N):
                for j in range(N):
                    if board[i][j] < 0: # 손님이 있는데 못태워줌. 실패
                        print(-1)
                        return
            print(F) # 모든 손님을 이미 다 태워줌
            return
        F -= tmp
        if F < 0: # 남은 손님이 있는데 데리러 가지 못함
            print(-1)
            return
        customer = -1 * board[taxi[0]][taxi[1]] #손님 index 구하고 태움
        board[taxi[0]][taxi[1]] = 0  # 손님 태웠으니 board에는 0으로 표시
        arrivePoint = arrive[customer] #해당 손님의 도착지점 구함
        tmp = goarrivepoint(board, taxi, arrivePoint, N)
        if tmp == -1: #목적지 도착 불가능
            print(-1)
            return
        F -= tmp
        if F < 0: #연료고갈
            print(-1)
            return
        usingFuel = tmp # 손님 픽업 - 목적지 도달까지 사용된 연료
        F += (2 * usingFuel)# 사용했던 연료 2배만큼 충전


def getnearcustomer(board, taxi, N): #가까운 customer가 없으면 -1리턴. 있으면 사용한 연료수 return하고 taxi 좌표 수정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    if board[taxi[0]][taxi[1]] < 0:
        return 0
    q.append([0, taxi[0], taxi[1]])
    visitChk = [[0 for i in range(N)] for j in range(N)]
    visitChk[taxi[0]][taxi[1]] = 1
    customer = []
    while len(q):
        y, x = q[0][1], q[0][2]
        for i in range(4):
            if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N and visitChk[y + dy[i]][x + dx[i]] == 0:
                if board[y + dy[i]][x + dx[i]] == 0:
                    q.append([q[0][0] + 1, y + dy[i], x + dx[i]])
                    visitChk[y + dy[i]][x + dx[i]] = 1
                if board[y + dy[i]][x + dx[i]] < 0:
                    customer.append([q[0][0] + 1, y + dy[i], x + dx[i]])
                    q.append([q[0][0] + 1, y + dy[i], x + dx[i]])
                    visitChk[y + dy[i]][x + dx[i]] = 1
        q.popleft()
    if len(customer) == 0: #도착가능한 손님 없음
        return -1
    else:
        customer.sort()
        taxi[0], taxi[1] = customer[0][1], customer[0][2]
        return customer[0][0]


def goarrivepoint(board, taxi, arrivePoint, N): #목적지에 도착 불가능하면 -1 리턴. 있으면 사용 연료수 return하고 taxi 좌표 수정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append([0, taxi[0], taxi[1]])
    visitChk = [[0 for i in range(N)] for j in range(N)]
    visitChk[taxi[0]][taxi[1]] = 1
    while len(q) > 0:
        y, x = q[0][1], q[0][2]
        for i in range(4):
            if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N and visitChk[y + dy[i]][x + dx[i]] == 0:
                if board[y + dy[i]][x + dx[i]] != 1:
                    if y + dy[i] == arrivePoint[0] and x + dx[i] == arrivePoint[1]:
                        taxi[0], taxi[1] = y + dy[i], x + dx[i]
                        return q[0][0] + 1
                    q.append([q[0][0] + 1, y + dy[i], x + dx[i]])
                    visitChk[y + dy[i]][x + dx[i]] = 1
        q.popleft()
    return -1


if __name__ == "__main__":
    main()
