import sys
def main():
    numbers = list(map(int, sys.stdin.readline().split()))
    ln = len(numbers)
    answer = 0
    for i in range(ln):
        answer += pow(numbers[i], 2)
    print(answer % 10)

if __name__ == "__main__":
    main()
