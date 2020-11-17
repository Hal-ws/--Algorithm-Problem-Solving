import sys


def main():
    R, C = map(int, sys.stdin.readline().split())
    forest = []
    for i in range(R):
        forest.append(sys.stdin.readline()[:C])
        if "S" in forest[i]:
            start = [i, forest[i].index("S")]
    



if __name__ == "__main__":
    main()
