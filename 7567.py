def main():
    dishes = list(input())
    ld = len(dishes)
    ans = 10
    for i in range(1, ld):
        if dishes[i] != dishes[i - 1]:
            ans += 10
        else:
            ans += 5
    print(ans)


if __name__ == "__main__":
    main()
