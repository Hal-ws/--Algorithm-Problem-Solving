def main():
    N = int(input())
    if N == 0:
        print(0)
    else:
        print(positive(N))


def positive(N):
    ans = ''
    if N == 1:
        return '1'
    while 1:
        if N == 1:
            return '1' + ans
        if N % 2 == 0:
            ans = '0' + ans #0 갖다붙임
            N = N // (-2)
        else:
            ans = '1' + ans
            N = N // (-2) + 1


if __name__ == '__main__':
    main()
