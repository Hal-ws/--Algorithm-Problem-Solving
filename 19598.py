import sys
from queue import PriorityQueue


def main():
    N = int(sys.stdin.readline())
    schedule = []
    endTime = PriorityQueue()
    for i in range(N):
        start, end = map(int, sys.stdin.readline().split())
        schedule.append([start, end])
    schedule.sort()
    endTime.put(schedule[0][1])
    cnt = 1
    ans = 0
    for i in range(1, N):
        nxtStart = schedule[i][0]
        while 1:
            if cnt == 0:
                break
            nearEnd = endTime.get()
            if nxtStart < nearEnd:  # 아직 안끝남
                endTime.put(nearEnd)
                break
            else: #가장 가까운 end가 끝남
                cnt -= 1
        cnt += 1
        endTime.put(schedule[i][1])
        if ans <= cnt:
            ans = cnt
    print(ans)


if __name__ == "__main__":
    main()
