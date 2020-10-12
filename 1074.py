N, r, c = map(int, input().split())


def getans(length, r, c, maxVal):
    if length == 1:
        return maxVal
    if r < (length // 2) and c < (length // 2):
        return getans(length // 2, r, c, maxVal - (length * length // 4 * 3))
    elif r < (length // 2) <= c:
        return getans(length // 2, r, c - length // 2, maxVal - (length * length // 4 * 2))
    elif r >= (length // 2) > c:
        return getans(length // 2, r - length // 2, c, maxVal - (length * length // 4 * 1))
    else:
        return getans(length // 2, r - length // 2, c - length // 2, maxVal)

print(getans(pow(2, N), r, c, pow(2, N) * pow(2, N) - 1))
