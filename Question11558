import sys

T = int(sys.stdin.readline())

def playGOD():
    players = []
    N = int(sys.stdin.readline())
    for i in range(N):
        players.append(int(sys.stdin.readline()))
    pointer = 0
    for i in range(N):
        pointed = players[pointer] - 1
        if pointed == N - 1:
            return i + 1
        pointer = pointed
    return 0

for i in range(T):
    print(playGOD())
