import sys

a, b, c, d = map(str, sys.stdin.readline().split())
a = int(a + b)
c = int(c + d)
print(a + c)
