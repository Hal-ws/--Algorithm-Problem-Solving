def main():
    N, M = map(int, input().split())
    num = sorted(list(map(int, input().split())))
    idx = [0] * M
    list1 = []
    while True:
        temp = [0] * M
        for i in range(M):
            temp[i] = num[idx[i]]
        list1.append(temp)
        if temp[0] == num[N - 1]:
            break
        idx[M - 1] += 1
        for j in range(M - 1, 0, -1):
            if idx[j] == N:
                idx[j - 1] += 1
                idx = idx[:j] + [idx[j - 1]] * (N - j)
    list1.sort()
    ans = [list1[0]]
    l1 = len(list1)
    std = 0
    for i in range(1, l1):
        if list1[i] != ans[std]:
            ans.append(list1[i])
            std += 1
    la = len(ans)
    for i in range(la):
        for j in range(M):
            print(ans[i][j], end=' ')
        print()


if __name__ == "__main__":
    main()
