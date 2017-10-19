from math import sqrt

x1, y1 = input().split(' ')
x2, y2 = input().split(' ')


d = sqrt((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)
d = format(d, '.4f')

print(d)
