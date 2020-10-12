import sys

N, K = map(int, sys.stdin.readline().split())
numbers = [0] * N
for i in range(N):
    numbers[i] = i + 1

cd = K - 1
ans = []
length = len(numbers)
i = 0
while True:
    ans.append(numbers[cd])
    numbers.remove(numbers[cd])
    length -= 1
    if length == 0:
        break
    cd = (K + cd - 1) % length
    i += 1

print('<', end='')
for i in range(N - 1):
    print(ans[i], end = ', ')
print(str(ans[N - 1]) + '>')
