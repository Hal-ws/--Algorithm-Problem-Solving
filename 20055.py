from collections import deque


def main():
    N, K = map(int, input().split())
    upper = deque()
    lower = deque()
    robots = deque()
    dura = list(map(int, input().split()))
    for i in range(2 * N):
        if i < N:
            upper.append(dura[i])
            robots.append(0)
        else:
            lower.appendleft(dura[i])
    step = 1
    while 1:
        rotatebelt(upper, lower, robots, N) #벨트 한 칸 회전. 끝에 있던 로봇은 떨어진다
        moverobot(upper, robots, N) #로봇 움직임. 맨 끝에 있던 로봇은 내려간다.
        setrobot(upper, robots) #로봇 셋팅
        if upper.count(0) + lower.count(0) >= K:
            break
        step += 1
    print(step)


def rotatebelt(upper, lower, robots, N):
    lower.append(upper.pop())
    upper.appendleft(lower.popleft())
    robots.pop()
    robots.appendleft(0)
    if robots[N - 1] == 1:
        robots[N - 1] = 0


def moverobot(upper, robot, N):
    for i in range(N - 2, -1, -1):
        if robot[i] == 1:
            if robot[i + 1] == 0 and upper[i + 1] > 0:
                upper[i + 1] -= 1
                robot[i + 1] = 1
                robot[i] = 0
    if robot[N - 1] == 1:
        robot[N - 1] = 0


def setrobot(upper, robots):
    if upper[0] != 0 and robots[0] == 0: # 내구도 남아있고, 로봇도 없음
        robots[0] = 1
        upper[0] -= 1 # 올라가서 내구도 감소


if __name__ == "__main__":
    main()
