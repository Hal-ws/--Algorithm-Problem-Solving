import sys

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

candidates = []
for i in range(4):
    candidates.append(A / C + B / D)
    temp = D
    D = B
    B = A
    A = C
    C = temp

print(candidates.index(max(candidates)))
