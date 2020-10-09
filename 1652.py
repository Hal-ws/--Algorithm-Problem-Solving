import sys

N = int(sys.stdin.readline())
room = [0] * N

for i in range(N):
    room[i] = sys.stdin.readline()

pAns = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if room[i][j] == '.':
            cnt += 1
        if room[i][j] == 'X' or j == N - 1:
            if cnt >= 2:
                pAns += 1
            cnt = 0
vAns = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if room[j][i] == '.':
            cnt += 1
        if room[j][i] == 'X' or j == N - 1:
            if cnt >= 2:
                vAns += 1
            cnt = 0

print(str(pAns) + ' ' + str(vAns))
