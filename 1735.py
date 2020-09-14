from math import gcd

a, b = map(int, input().split())
c, d = map(int, input().split())
up = a * d + b * c
down = b * d
while 1:
    devide = gcd(up, down)
    up, down = up // devide, down // devide
    if devide == 1:
        break

print('%s %s' %(up, down))
