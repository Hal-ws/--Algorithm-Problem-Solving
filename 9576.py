import sys


def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        print(getmaxstudent())
    return 0


def getmaxstudent():
    N, M = map(int, sys.stdin.readline().split())
    wishList = []
    for i in range(M):
        wishList.append(list(map(int, sys.stdin.readline().split())))
    wishList = sorted(wishList)
    return 0
    

if __name__ == "__main__":
    main()
