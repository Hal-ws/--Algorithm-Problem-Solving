def main():
    N = int(input())
    print(getfibo(N) % 10007)


def getfibo(N):
    if N <= 2:
        return N
    first = 1
    second = 2
    for i in range(N - 2):
        temp = first
        first = second
        second = first + temp
    return second


if __name__ == "__main__":
    main()
