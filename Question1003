T = int(input())

def fibonacci(n):
    first = 0
    second = 1
    if(n <= 1):
        return n
    else:
        i = 2
        while(i <= n):
            sum = first + second
            first = second
            second = sum
            i += 1
        return sum

i = 0
while(i < T):
    N = int(input())
    if(N == 0):
        print('1 0')
    else:
        print(str(fibonacci(N - 1)) + ' ' + str(fibonacci(N)))
    i += 1
