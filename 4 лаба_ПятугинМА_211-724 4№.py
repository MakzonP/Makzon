import tkinter.messagebox as mb

a = int(input('¬ведите число а '))
b = int(input('¬ведите число b '))

if a == 0 or b == 0:
    mb.showerror('ERROR', 'a не должно быть равно 0')
else:
    print(a + b)
    print(a - b)
    print(a * b)
    print(a**2 / b**2)