import sys
sys.setrecursionlimit(pow(10, 5) + 1)


def main():
    T = int(sys.stdin.readline())
    global choice, chk, visit
    for _ in range(T):
        n = int(sys.stdin.readline())
        choice = [0] + list(map(int, sys.stdin.readline().split()))
        chk = [0] * (n + 1) # 아직 안정해진 경우: 0, 가능: 1, 불가능: -1
        visit = [0] * (n + 1)
        for i in range(1, n + 1):
            if chk[i] == 0:
                visit[i] = 1
                chkCycle(i, choice[i])
                visit[i] = 0
        print(chk.count(-1))


def chkCycle(cur, nxt):
    global choice, chk, visit
    visit[cur] = 1
    if visit[nxt]: # 이미 방문했을 때
        chk[cur] = 1
        visit[cur] = 0
        if cur == nxt:
            return - 1
        return nxt # cycle의 시작점 return
    if chk[nxt] != 0 : # 이미 실패한게 확정인 경우
        chk[cur] = -1
        visit[cur] = 0
        return - 1 # 실패 return
    tmp = chkCycle(nxt, choice[nxt])
    visit[cur] = 0
    if tmp == -1: # 사이클 형성 실패
        chk[cur] = -1
        return -1
    else: # 사이클 형성 성공
        chk[cur] = 1
        if tmp == cur:
            return -1
        else:
            return tmp


if __name__ == '__main__':
    main()
