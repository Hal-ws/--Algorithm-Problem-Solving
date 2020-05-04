import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A_ = A

A_ = sorted(A_)
P = [0] * N
for i in range(N):
    P[i] = A_.index(A[i])
    A_[P[i]] = None

for i in range(N):
    print(P[i], end=' ')
