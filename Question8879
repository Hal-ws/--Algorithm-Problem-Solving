import sys

N, K = map(int, sys.stdin.readline().split())
countries = []

for i in range(N):
    country = list(map(int, sys.stdin.readline().split()))
    countries.append(country[1:])
    if country[0] == K:
        target = country[1:]

countries = sorted(countries, reverse=True)
for i in range(N):
    if countries[i] == target:
        print(i + 1)
        break
