n = int(input())

def getcycle():
    cycle = [0, 1]
    i = 2
    while True:
        cycle.append((cycle[i - 2] + cycle[i - 1]) % 1000000)
        if cycle[i - 1] == 0 and cycle[i] == 1:
            return cycle[:i - 1]
        i += 1

cycle = getcycle()
print(cycle[n % len(cycle)])
