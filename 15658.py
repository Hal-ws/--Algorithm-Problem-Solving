import sys


def main():
    N = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    signs = list(map(int, sys.stdin.readline().split()))
    results = set()
    dfs(signs[0], signs[1], signs[2], signs[3], results, 1, nums[0], nums, N)
    print(max(results))
    print(min(results))


def dfs(plus, minus, multi, devide, results, level, cur, nums, N):
    if level == N: # 이미 level개의 수를 계산했음
        results.add(cur)
        return
    if plus > 0:
        dfs(plus - 1, minus, multi, devide, results, level + 1, cur + nums[level], nums, N)
    if minus > 0:
        dfs(plus, minus - 1, multi, devide, results, level + 1, cur - nums[level], nums, N)
    if multi > 0:
        dfs(plus, minus, multi - 1, devide, results, level + 1, cur * nums[level], nums, N)
    if devide > 0:
        if cur >= 0:
            dfs(plus, minus, multi, devide - 1, results, level + 1, cur // nums[level], nums, N)
        else:
            next = -1 * (cur * (-1) // nums[level])
            dfs(plus, minus, multi, devide - 1, results, level + 1, next, nums, N)


if __name__ == "__main__":
    main()
