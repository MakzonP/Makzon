A = int(input('������� ���������� � '))
B = int(input('������� ���������� � '))
C = int(input('������� ���������� � '))
if A < C:
    dAC = C - A
else:
    dAC = A - C
print('����� ������� AC = ', dAC)

if B < C:
    dBC = C - B
else:
    dBC = B - C
print('����� ������� BC = ', dBC)

print('����� ���� �������� = ', dAC + dBC)