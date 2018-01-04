ok = False
while not ok:
    try:
        x = int(input('Inserisci un numero: '))
        ok = True
    except ValueError:
        print('Errore: non sono riuscito ad interpretare il valore inserito come un numero.')
        continue

print('Il quadrato di {} è {}.'.format(x, x**2))
