def main():
    start = list(input())
    target = list(input())
    ls, lt = len(start), len(target)
    while lt > ls:
        if target[lt - 1] == "B":
            del target[lt - 1]
            target.reverse()
        else:
            del target[lt - 1]
        lt -= 1
    if start == target:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
