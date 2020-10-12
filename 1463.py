N = int(input())

steps = [[N]]

cal = 1
if N == 1:
    print(0)
else:
    while True:
        temp = []
        for i in range(len(steps[0])):
            if steps[0][i] % 2 == 0:
                temp.append(steps[0][i] // 2)
            if steps[0][i] % 3 == 0:
                temp.append(steps[0][i] // 3)
            temp.append(steps[0][i] - 1)
        steps.append(temp)
        if 1 in steps[1]:
            print(cal)
            break
        steps[0] = steps[1]
        del steps[1]
        cal += 1
