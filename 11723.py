import sys


def main():
    M = int(sys.stdin.readline())
    S = [0] * 21
    for i in range(M):
        command = sys.stdin.readline()
        if command[0] == "a" and command[1] == "l":
            S = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 ,18, 19, 20]
        elif command[0] == "e" and command[1] == "m":
            S = [0] * 21
        else:
            first, second = map(str, command.split())
            x = int(second)
            if command[0] == "a":
                S[x] = x
            if command[0] == "r":
                S[x] = 0
            if command[0] == "c":
                if S[x] == x:
                    print(1)
                else:
                    print(0)
            if command[0] == "t":
                if S[x] == 0:
                    S[x] = x
                else:
                    S[x] = 0


if __name__ == "__main__":
    main()
