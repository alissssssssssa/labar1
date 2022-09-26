a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = b**2 - 4*a*c
if d > -1:
    d = d**0.5
    x1 = (b*(-1) + d)/(2*a)
    x2 = (b*(-1) - d)/(2*a)
    print('x1 = ', x1, 'x2 = ', x2)
else:
    print('корней нет')