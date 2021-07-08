import sys


def main():
    xs, ys = map(int, sys.stdin.readline().split())
    xe, ye = map(int, sys.stdin.readline().split())
    telPoints = []
    answer = 1000000001
    for i in range(3):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        telPoints.append([[x1, y1], [x2, y2]])
    
    print(answer)
    return
    
if __name__ == "__main__":
    main()
