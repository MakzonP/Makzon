import tkinter.messagebox as mb

a = int(input('������� ����� � '))
b = int(input('������� ����� b '))

if a == 0 or b == 0:
    mb.showerror('ERROR', 'a �� ������ ���� ����� 0')
else:
    print(a + b)
    print(a - b)
    print(a * b)
    print(a**2 / b**2)