N = int(input())

first = 1
second = 2
if N < 3:
    print(N)
else:
    for i in range (N - 2):
        nthAns = first + second
        if (nthAns >= 15746):
            nthAns -= 15746
        first = second
        second = nthAns
    print(nthAns)
