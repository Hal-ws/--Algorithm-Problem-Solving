import sys
from itertools import product


def main():
    M, S = map(int, sys.stdin.readline().split())
    paths = list(product([0, 1, 2, 3], 3))
    fBoard =[[[] for j in range(4)] for i in range(4)]
    eBoard = [[[] for j in range(4)] for i in range(4)]
