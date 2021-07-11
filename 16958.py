import sys


def main():
  N, T = map(int, sys.stdin.readline().split())
  for _ in range(N):
    s, x, y = map(int, sys.stdin.readline().split())
  M = int(sys.stdin.readline())
  for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    print(getMintime(A, B))
  return 0


def getMinTime():
  return 0

if __name__ == "__main__":
  main()
