import tkinter.messagebox as mb

A = int(input('������� ���������� � '))
B = int(input('������� ���������� � '))
C = int(input('������� ���������� � '))
if (C > A and C < B) or (C > B and C < A):
    if A < C:
        dAC = C - A
    else:
        dAC = A - C
    print('����� �� = ', dAC)
        
    if B < C:
        dBC = C - B
    else:
        dBC = B - C
    print('����� �� = ', dBC)    
        
    print('������������ ���� �������� = ', dAC * dBC)
else:
    mb.showerror('ERROR', '� ������ ���������� ����� � � �')