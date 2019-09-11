import sys
N = int(input())

ropes = []
for i in range(N):
    ropes.append(int(sys.stdin.readline()))
ropes = sorted(ropes)
weight = []
i = 1
while(i <= len(ropes)):
    weight.append(ropes[len(ropes) - i] * i)
    i += 1

print(max(weight))
