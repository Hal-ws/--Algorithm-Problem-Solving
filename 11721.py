inputStr = str(input())

i = 0
while(i < len(inputStr)):
    j = 0
    answer = ''
    while(j < 10 and i < len(inputStr)):
        answer = answer + inputStr[i]
        i += 1
        j += 1
    print(answer)
