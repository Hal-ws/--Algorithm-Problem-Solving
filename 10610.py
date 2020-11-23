def main():
    num = list(map(int, input()))
    if sum(num) % 3 == 0:
        num = sorted(num, reverse=True)
        if num[-1] == 0:
            for i in range(len(num)):
                print(num[i], end='')
        else:
            print(-1)
    else:
        print(-1)


if __name__ == "__main__":
    main()
