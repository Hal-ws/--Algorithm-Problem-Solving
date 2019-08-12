N = input()
standard = N
cycle = 0
while(True):
    cycle += 1
    if(len(N) < 2): ## 10 미만의 수 입력
        N =  '0' + N
    sum = int(N[0]) + int(N[1])
    if(sum < 10 and N[1] != '0'):
        newN = N[1] + str(sum)
    elif(sum >= 10 and N[1] != '0'):
        newN = N[1] + str(sum)[1]
    elif(sum < 10 and N[1] == '0'):
        newN = str(sum)
    else:
        newN = str(sum)[1]
    if(newN == standard):
        print(cycle)
        break
    else:
        N = newN
