def main():
    T = int(input())
    for i in range(T):
        n = int(input())
        upperside = list(map(int, input().split()))
        downside = list(map(int, input().split()))
        print(getans(upperside, downside, n))


def getans(upperside, downside, n):
    maxupper = [upperside[0]] +  [0] * (n - 1)
    maxdownside = [downside[0]] + [0] * (n - 1)
    for i in range(1, n):
        if i == 1:
            maxupper[i] = upperside[i] + downside[i - 1]
            maxdownside[i] = downside[i] + upperside[i - 1]
        else:
            maxupper[i] = max(maxupper[i - 2], maxdownside[i - 2], maxdownside[i - 1]) + upperside[i]
            maxdownside[i] = max(maxupper[i - 2], maxupper[i - 1], maxdownside[i - 2]) + downside[i]
    if n == 1:
        return max(maxupper[0], maxdownside[0])
    else:
        return max(maxupper[n - 2], maxupper[n - 1], maxdownside[n - 2], maxdownside[n - 1])


if __name__ == "__main__":
    main()
