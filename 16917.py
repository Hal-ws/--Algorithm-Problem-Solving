def main():
    A, B, C, X, Y = map(int, input().split())
    price = 0
    if (A + B) / 2 >= C:
        half = min(X, Y) * 2 # 양념, 후라이드중 적게 시키는거를 half로 맞춘다. half 치킨수
        price += half * C
        X -= (half // 2)
        Y -= (half // 2)
        if A / 2 >= C:
            price += 2 * X * C
            X = 0
        if B / 2 >= C:
            price += 2 * Y * C
            Y = 0
    price += X * A
    price += Y * B
    print(price)


if __name__ == "__main__":
    main()
