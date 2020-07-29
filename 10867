import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))
count = [0] * 2001

for i in range(N):
    if count[numbers[i] + 1000] == 0:
        count[numbers[i] + 1000] = 1
for i in range(2001):
    if count[i]:
        print(i - 1000, end =' ')
