def main():
    N, B = map(int, input().split())
    ans = ''
    while N >= B:
        val = N % B
        N = N // B
        if val >= 10:
            val = chr(val + 55)
        else:
            val = str(val)
        ans = val + ans
    if N >= 10:
        N = chr(N + 55)
    else:
        N = str(N)
    ans = N + ans
    print(ans)


if __name__ == '__main__':
    main()
