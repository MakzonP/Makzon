import tkinter.messagebox as mb

A = int(input('ââåäèòå êîîğäèíàòó À '))
B = int(input('ââåäèòå êîîğäèíóòà Â '))
C = int(input('ââåäèòå êîîğäèíàòó Ñ '))
if (C > A and C < B) or (C > B and C < A):
    if A < C:
        dAC = C - A
    else:
        dAC = A - C
    print('äëèíà ÀÑ = ', dAC)
        
    if B < C:
        dBC = C - B
    else:
        dBC = B - C
    print('äëèíà ÂÑ = ', dBC)    
        
    print('Ïğîèçâåäåíèå äëèí îòğåçêîâ = ', dAC * dBC)
else:
    mb.showerror('ERROR', 'Ñ äîëæíî íàõîäèòüñÿ ìåæäó À è Â')