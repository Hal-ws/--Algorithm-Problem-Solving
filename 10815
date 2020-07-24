def main():
    global  N
    global M
    N = int(input())
    havingCards = list(map(int, input().split()))
    havingCards = sorted(havingCards)
    M = int(input())
    numCards = list(map(int, input().split()))
    ans = [0] * M
    for i in range(M):
        ans[i] = binary(havingCards, numCards[i])
    for i in range(M):
        print(ans[i], end = ' ')

def binary(list, target):
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return 1
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0
if __name__ == "__main__":
    main()
