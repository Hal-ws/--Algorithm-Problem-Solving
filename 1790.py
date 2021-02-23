def main():
    N, K = map(int, input().split())
    nLen = 0 # 1부터 N까지 쓰면서 생기는 수의 길이 저장
    l = len(str(N))
    for i in range(1, l): # 길이 1 ~ l - 1까지 길이 저장
        nLen += 9 * pow(10, i - 1) * i
    nLen += (N - pow(10, l - 1) + 1) * l
    if nLen < K:  # N까지 적어도
        print(-1)
        return
    size = 1 # 적어가는 숫자들의 각각 크기
    while 1:
        tLen = size * 9 * pow(10, size - 1) # 총 길이
        if K <= tLen:
            maxSize = size # 답이 되는 숫자의 길이
            break
        size += 1
    for i in range(1, maxSize):
        K -= 9 * i * pow(10, i - 1)
    if K % maxSize == 0:
        lastNum = str(pow(10, maxSize - 1) - 1 + K // maxSize) #마지막으로 오는 숫자
        print(lastNum[-1])
    else: # 나머지가 있을 때
        lastNum = str(pow(10, maxSize - 1) - 1 + K // maxSize + 1)
        print(lastNum[K % maxSize - 1])


if __name__ == '__main__':
    main()
