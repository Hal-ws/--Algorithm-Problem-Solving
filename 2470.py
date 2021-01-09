def main():
    N = int(input())
    nList = list(map(int, input().split()))
    nList.sort()
    minVal = 2000000001
    ans = [0, 0]
    i, j = 0, N - 1
    while i < j:
        tmp = nList[i] + nList[j]
        if abs(tmp) < minVal:
            minVal = abs(tmp)
            ans[0], ans[1] = nList[i], nList[j]
        if tmp > 0:
            j -= 1
        elif tmp < 0:
            i += 1
        else:
            break
    print('%s %s' %(ans[0], ans[1]))


if __name__ == '__main__':
    main()
