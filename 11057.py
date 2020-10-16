def main():
    N = int(input())
    ansList = [1] * 10
    for i in range(N - 1):
        for j in range(10):
            ansList[j] = sum(ansList[j:10])
    print(sum(ansList) % 10007)

if __name__ == "__main__":
    main()
