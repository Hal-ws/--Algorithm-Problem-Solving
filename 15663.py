from itertools import permutations


def main():
    N, M = map(int, input().split())
    num = sorted(list(map(int, input().split())))
    list1 = sorted(list((permutations(num, M))))
    l1 = len(list1)
    ans = [list1[0]]
    standard = 0
    for i in range(1, l1):
        if list1[i] != ans[standard]:
            ans.append(list1[i])
            standard += 1
    la = len(ans)
    for i in range(la):
        for j in range(M):
            print(ans[i][j], end= ' ')
        print()


if __name__ == "__main__":
    main()
