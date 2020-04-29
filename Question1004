import sys
T = int(sys.stdin.readline())

def checkpass(p1, p2, c):
    if ((c[0] - p1[0]) * (c[0] - p1[0]) + (c[1] - p1[1]) * (c[1] - p1[1]) > c[2] * c[2]) != ((c[0] - p2[0]) * (c[0] - p2[0]) + (c[1] - p2[1]) * (c[1] - p2[1]) > c[2] * c[2]) :
        return True

for i in range(T):
    points = list(map(int, sys.stdin.readline().split()))
    n = int(sys.stdin.readline())
    planets = []
    cnt = 0
    for j in range(n):
        planets.append(list(map(int, sys.stdin.readline().split())))
    for k in range(n):
        if checkpass([points[0], points[1]], [points[2], points[3]], planets[k]):
            cnt += 1
    print(cnt)
