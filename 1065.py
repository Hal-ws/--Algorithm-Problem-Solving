N = int(input())

def checkHansu(num):
    if(num < 100): ## 100보다 작은 모든 값은 다 한수이다
        return True
    else:
        strVal = str(num)
        d =int(strVal[1]) - int(strVal[0]) ## 공차
        i = 1
        while(i < len(strVal) - 1):
            if(int(strVal[i + 1]) - int(strVal[i]) != d):
                return False
            i += 1
        return True

i = 1
ans = 0
while(i <= N):
    if(checkHansu(i)):
        ans += 1
    i += 1

print(ans)
