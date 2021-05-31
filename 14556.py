def main():
    N = int(input())
    answer = 1
    mulFactor = 3
    for i in range(1, N):
        answer = answer * mulFactor % 1000000009
        mulFactor += 2
    print(answer)


if __name__ == '__main__':
    main()
