a = eval(input('Inserisci il coefficiente a: '))
b = eval(input('Inserisci il coefficiente b: '))
c = eval(input('Inserisci il coefficiente c: '))

delta = b**2 - 4*a*c

formatted_eq = '{}x^2 + {}x + {} = 0'.format(a, b, c)

if delta < 0:
    print('L\'equazione', formatted_eq, 'non ha soluzioni reali.')
else:
    if delta == 0:
        x = -b/(2*a)
        print('L\'equazione', formatted_eq, 'ha una soluzione reale:')
        print('x = {}.'.format(x))
    else:
        x1 = (-b+delta**.5)/(2*a)
        x2 = (-b-delta**.5)/(2*a)
        print('L\'equazione', formatted_eq, 'ha due soluzioni reali:')
        print('x1 = {}, x2 = {}.'.format(x1, x2))
