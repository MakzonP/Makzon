import tkinter.messagebox as mb

A = int(input('������� ����� ������������� ����� � '))
B = int(input('������� ����� ������������� ����� B '))
c = 0

if A < B:
    mb.showerror('ERROR', '����� � ������ ���� ������ �')
else:
    while A >= B:
        A -= B

print('����� ��������� ����� ������� � ����� ', A)