import math
import sys

def checkSosu(number): ## 주어진 number가 소수인지 체크
    i = 2
    while(i <= math.sqrt(number)):
        if(number % i == 0):
            return False
        else:
            i += 1
    return True

def getGoldbach(inputnumber):
    i = 2
    while(i <= (inputnumber // 2)):
        if(checkSosu(i) and checkSosu(inputnumber - i)):
            print(str(inputnumber) + ' = ' + str(i) + ' + ' + str(inputnumber - i))
            return i
        else:
            i += 1
    print('Goldbach'+'s' + 'conjecture is wrong')

i = 0
while 1:
    inputnumber = int(sys.stdin.readline())
    if inputnumber == 0:
        break
    else:
        getGoldbach(inputnumber)
    i += 1
