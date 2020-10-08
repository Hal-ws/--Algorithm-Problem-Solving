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
        if sum(temp) == num[N - 1] * M:
            break
        idx[M - 1] += 1
        for i in range(M - 1, 0, -1):
            if idx[i] == N:
                idx[i - 1] +=1
                idx[i] = 0
    list1.sort()
    ans, std = [list1[0]], 0
    l1 = len(list1)
    for i in range(1, l1):
        if list1[i] != ans[std]:
            ans.append(list1[i])
            std += 1
    la = len(ans)
    for i in range(la):
        for j in range(M):
            print(ans[i][j], end= ' ')
        print()


if __name__ == "__main__":
    main()
