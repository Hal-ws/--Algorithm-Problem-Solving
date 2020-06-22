a, b, c = map(int, input().split())

def powers(a, b, c):
    if b == 0:
        return 1
    n = powers(a, b // 2, c)
    if b % 2 == 0:
        return (n * n) % c
    else:
        return (a * n * n) % c

print(powers(a, b, c))
