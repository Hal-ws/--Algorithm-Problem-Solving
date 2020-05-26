first = sorted(input())
second = sorted(input())
def getsame(short, long):
    same = 0
    i = 0
    j = 0
    while i < len(short) and j < len(long):
        if short[i] == long[j]:
            same += 1
            i += 1
            j += 1
        elif short[i] > long[j]:
            j += 1
        else:
            i += 1
    return same
ans = 0
if len(first) >= len(second):
    ans += (len(first) - len(second))
    ans += (len(second) - getsame(second, first)) * 2
    print(ans)
else:
    ans += (len(second) - len(first))
    ans += (len(first) - getsame(first, second)) * 2
    print(ans)

