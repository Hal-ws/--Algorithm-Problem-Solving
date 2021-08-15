import sys
from math import inf


def main():
    N, T = map(int, sys.stdin.readline().split())
    cityinfos = []
    for _ in range(N):
        cityinfos.append(list(map(int, sys.stdin.readline().split())))
    disMatrix = [[0 for j in range(N + 1)] for i in range(N + 1)]
    M = int(sys.stdin.readline())
    
