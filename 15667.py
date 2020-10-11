N = int(input())

for k in range(1, N + 1):
    if k * k + k == N - 1:
        print(k)
        break
