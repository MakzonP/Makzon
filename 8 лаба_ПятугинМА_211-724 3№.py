import tkinter.messagebox as mb

A = int(input('Введите целое положительное число А '))
B = int(input('Введите целое положительное число B '))
c = 0

if A < B:
    mb.showerror('ERROR', 'Число А должно быть больше В')
else:
    while A >= B:
        A -= B

print('Длина незанятой части отрезка А равна ', A)