X = int(input())

def getans(x):
    for i in range(7):
        if x == (2 ** i):
            return 1
        elif x < (2 ** i):
            val = i - 1
            break
    return getans(2 ** val) + getans(x - 2 ** val)

print(getans(X))
