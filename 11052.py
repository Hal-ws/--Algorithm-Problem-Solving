def main():
    N = int(input())
    cards = [0] + list(map(int, input().split()))
    cost = [0] * (N + 1)
    cost[1] = cards[1]
    for i in range(2, N + 1):
        maxCost = cards[i]
        for j in range(1, i // 2 + 1):
            if maxCost <= (cost[j] + cost[i - j]):
                maxCost = (cost[j] + cost[i - j])
        cost[i] = maxCost
    print(cost[N])

    
if __name__ == "__main__":
    main()
