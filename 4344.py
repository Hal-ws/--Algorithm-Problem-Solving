C = int(input())

i = 1
while(i <= C):
    case = list(map(int, input().split()))
    average = (sum(case) - case[0]) / case[0]
    j = 1
    numOverAverage = 0
    while(j < len(case)):
        if(case[j] > average):
            numOverAverage += 1
            j += 1
        else:
            j += 1
    print(str(format(round(100 * numOverAverage / (len(case) - 1), 3), '.3f') + '%'))
    i += 1
