import sys


def main():
    height, wide = map(int, sys.stdin.readline().split())
    using = int(sys.stdin.readline()) # 사용하는 종이의 갯수
    wrongs = int(sys.stdin.readline())
    wrongPositions = []
    for i in range(wrongs):
        x, y = map(int, sys.stdin.readline().split())
        wrongPositions.append([x, y])
    left, right = 1, min(height, wide)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if covering(wrongPositions, using, mid): # cover 가능. 사이즈 더 줄여봄
            right = mid - 1
            answer = mid
        else: # 불가능. 사이즈 늘림
            left = mid + 1
    print(answer)


def covering(wrongPositions, using, size):
    
    return 1


if __name__ == "__main__":
    main()

