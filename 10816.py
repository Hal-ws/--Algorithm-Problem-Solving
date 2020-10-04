def main():
    N = int(input())
    havingCards = list(map(int, input().split()))
    M = int(input())
    chkCard = list(map(int, input().split()))
    havingCards = sorted(havingCards)
    ans = [0] * M
    for i in range(M):
        ans[i] = upperbound(chkCard[i], havingCards) - lowerbound(chkCard[i], havingCards)
    for i in range(M):
        print(ans[i], end = ' ')

def upperbound(card, havingCards):
    low = 0
    high = len(havingCards)
    while low < high:
        mid = (low + high) // 2
        if card >= havingCards[mid]:
            low = mid + 1
        else:
            high = mid
    return low

def lowerbound(card, havingCards):
    low = 0
    high = len(havingCards)
    while low < high:
        mid = (low + high) // 2
        if card <= havingCards[mid]:
            high = mid
        else:
            low = mid + 1
    return low

if __name__ == "__main__":
    main()
