import sys

N = int(input())
schedule = []
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    schedule.append([end, start])

schedule = sorted(schedule)

a = 1
b = 0
cnt = 1
endTime = schedule[0][0]
i = 1
while i < N:
    if schedule[i][1] >= endTime:
        cnt += 1
        endTime = schedule[i][0]
    i += 1

print(cnt)
