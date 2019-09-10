N = int(input())

persons = list(map(int, input().split()))
persons = sorted(persons)
sum = 0
accumulated = 0
i = 0
while(i < N):
    sum += (accumulated + persons[i])
    accumulated += persons[i]
    i += 1

print(sum)
