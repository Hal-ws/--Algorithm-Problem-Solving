import sys

def main():
    N = int(sys.stdin.readline())
    candidaters = list(map(int, sys.stdin.readline().split()))
    answer = 0
    B, C = map(int, sys.stdin.readline().split())
    for i in range(N):
        candidaters[i] -= B
        answer += 1
        if candidaters[i] < 0:
            candidaters[i] = 0
    print(answer + getSupervisors(N, C, candidaters))


def getSupervisors(N, a, candidaters):
    cnt = 0
    for i in range(N):
        if candidaters[i] % a == 0:
            cnt += candidaters[i] // a
        else:
            cnt += candidaters[i] // a + 1
    return cnt


if __name__ == "__main__":
    main()
