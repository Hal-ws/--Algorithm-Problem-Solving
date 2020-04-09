import sys

points = [list(map(int, sys.stdin.readline().split()))]
points.append([(points[0][0] + points[0][1]) / 2, 2 * points[0][0] * points[0][1] / (points[0][0] + points[0][1])])
i = 1
while points[i - 1] != points[i]:
	points.append([(points[i][0] + points[i][1]) / 2, 2 * points[i][0] * points[i][1] / (points[i][0] + points[i][1])])
	i += 1
	
print(str(points[i][0]) + ' ' + str(points[i][1]))
