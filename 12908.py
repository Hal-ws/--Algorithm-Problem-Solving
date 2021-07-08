import sys
from itertools import permutations



def main():
    xs, ys = map(int, sys.stdin.readline().split())
    xe, ye = map(int, sys.stdin.readline().split())
    telPoints = []
    answer = abs(xe - xs) + abs(ye - ys)
    for i in range(3):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        telPoints.append([x1, y1, i + 1])
        telPoints.append([x2, y2, i])
    paths = permutations(telPoints)
    for path in paths:
        time = gettime(path, xs, ys, xe, ye)
        if time < answer:
            answer = time
    print(answer)
    return


def gettime(path, xs, ys, xe, ye):
    cx, cy = path[0][0], path[0][1]
    result = abs(xe - xs) + abs(ye - ys)
    time = abs(cx - xs) + abs(cy - ys)
    curP = path[0][2]
    for i in range(1, 6):
        nxtP = path[i]
        nx, ny, nPnt = nxtP[0], nxtP[1], nxtP[2]

    return result


if __name__ == "__main__":
    main()
