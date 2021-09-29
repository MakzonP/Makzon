A = int(input('введите координату А '))
B = int(input('введите координута В '))
C = int(input('введите координату С '))
if A < C:
    dAC = C - A
else:
    dAC = A - C
print('длина отрезка AC = ', dAC)

if B < C:
    dBC = C - B
else:
    dBC = B - C
print('длина отрезка BC = ', dBC)

print('сумма длин отрезков = ', dAC + dBC)