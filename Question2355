numbers = list(map(int, input().split()))

numbers = sorted(numbers)
A = numbers[0]
B = numbers[1]

if A < 0 and B < 0:
    sumA = -((-A) * (-A + 1) // 2)
    sumB = -((-B) * (-B + 1) // 2)
    ans = sumA - sumB + B
elif A < 0 and B >= 0:
    sumA = -((-A) * (-A + 1) // 2)
    sumB = B * (B + 1) // 2
    ans = sumB + sumA
else:
    sumA = A * (A + 1) // 2
    sumB = B * (B + 1) // 2
    ans = sumB - sumA + A
print(ans)
