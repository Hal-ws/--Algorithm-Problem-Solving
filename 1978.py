N = int(input())
b = list(map(int, input().split()))

def checkSosu(number):
    if(number == 1):
        return False
    elif(number <= 3):
        return True
    else:
        i = 2
        while(i <= number // 2):
            if(number % i == 0): ## 나누어 떨어지면
                return False
            else:
                i += 1
    return True

i = 0
answer = 0
while(i < len(b)):
    if(checkSosu(b[i])):
        answer += 1
    i += 1

print(answer)
