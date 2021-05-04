import sys


def main():
    D, N = map(int, sys.stdin.readline().split())
    hSizes = list(map(int, sys.stdin.readline().split()))
    pizzas = list(map(int, sys.stdin.readline().split()))
    passSize = [0 for j in range(D)]
    passSize[0] = hSizes[0]
    for i in range(1, D):
        passSize[i] = min(passSize[i - 1], hSizes[i])
    mostDepth = D - 1
    for pSize in pizzas: #pSize보다 같거나 큰 passSize 중 가장 오른쪽에 있는 index를 찾아야함
        left, right = 0, mostDepth
        if mostDepth == -1 or passSize[left] < pSize: # 빈 곳이 없을때 또는 첫칸도 통과를 못할때
            print(0)
            return
        while left <= right:
            mid = (left + right) // 2
            if passSize[mid] < pSize: # 더 큰곳(왼쪽으로) 가야함
                right = mid - 1
            if passSize[mid] >= pSize: # 통과 가능하지만 끝까지 가야함
                left = mid
            if left == right:
                mostDepth = left - 1
                break
            if left == right - 1: # 붙어있을경우
                if passSize[right] >= pSize:
                    mostDepth = right - 1
                else:
                    mostDepth = left - 1
                break
    print(mostDepth + 2)


if __name__ == '__main__':
    main()
