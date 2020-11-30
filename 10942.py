import sys


def main():
    N = int(sys.stdin.readline())
    numbers = [0] + list(map(int, sys.stdin.readline().split()))
    dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
    for l in range(1, N + 1): #길이가 N인지 구함
        for s in range(1, N - l + 2):
            e = s + l - 1 #끝 idx
            if s == e:
                dp[s][e] = 1
            elif s == e - 1:
                if numbers[e] == numbers[s]:
                    dp[s][e] = 1
            else:
                if dp[s + 1][e - 1] == 1 and numbers[s] == numbers[e]:
                    dp[s][e] = 1
    M = int(sys.stdin.readline())
    for i in range(M):
        S, E = map(int, sys.stdin.readline().split())
        print(dp[S][E])
    

if __name__ == "__main__":
    main()
