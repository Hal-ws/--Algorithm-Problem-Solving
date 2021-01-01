import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    minSetPrice = 1001
    minOnePrice = 1001
    ans = 0
    for i in range(M):
        setPrice, onePrice = map(int, sys.stdin.readline().split())
        if setPrice <= minSetPrice:
            minSetPrice = setPrice
        if onePrice <= minOnePrice:
            minOnePrice = onePrice
    if minOnePrice * 6 <= minSetPrice:
        ans = N * minOnePrice
    else:
        while N > 0:
            if N >= 6:
                bulk = N // 6
                N -= 6 * bulk
                ans += minSetPrice * bulk
            else:
                piecePrice = N * minOnePrice
                if piecePrice <= minSetPrice:
                    ans += piecePrice
                else:
                    ans += minSetPrice
                N = 0
    print(ans)


if __name__ == '__main__':
    main()
