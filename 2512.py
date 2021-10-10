import sys


def main():
    N = int(sys.stdin.readline())
    nList = list(map(int, sys.stdin.readline().split()))
    budget = int(sys.stdin.readline())
    ans = 0
    left, right = 0, max(nList)
    if sum(nList) <= budget:
        print(right)
        return
    while left <= right:
        mid = (left + right) // 2
        tmpBudget = 0
        for money in nList:
            if money < mid:
                tmpBudget += money
            else:
                tmpBudget += mid
        if tmpBudget > budget:
            right = mid - 1
        else:
            left = mid + 1
            ans = mid
    print(ans)
    return


if __name__ == "__main__":
    main()
