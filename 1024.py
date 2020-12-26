def main():
    N, L = map(int, input().split())
    for l in range(L, 101):
        tmp = getAns(N, l)
        if tmp != None:
            for i in range(l):
                print(tmp[i], end=' ')
            return
    print(-1)


def getAns(N, l):
    std = N // l
    for start in range(std - l + 1, std + 1):
        if start >= 0:
            tmpSum = l * (start + start + l - 1) // 2
            if tmpSum == N:
                ans = []
                for i in range(l):
                    ans.append(start + i)
                return ans
    return None


if __name__ == '__main__':
    main()
