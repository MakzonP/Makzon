A1 = int(input('������� ���������� �1 '))
B1 = int(input('������� ���������� B1 '))
C1 = int(input('������� ���������� C1 '))
A2 = int(input('������� ���������� �2 '))
B2 = int(input('������� ���������� B2 '))
C2 = int(input('������� ���������� C2 '))

def F(A1, B1):
    return(A1 * x + B1 * y)
def F(A2, B2):
    return(A2 * x + B2 * y)

for x in range(0, 100):
    for y in range(0, 100):
        if F(A1, B1) == C1 and F(A2, B2) == C2:
            print(x, y)