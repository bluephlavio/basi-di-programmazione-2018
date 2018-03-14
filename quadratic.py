# Risolve una equazione di secondo grado dati i coefficienti a, b e c.

# Prendi i coefficienti a, b e c dallo stdin
a = eval(input('Inserisci il coefficiente a: '))
b = eval(input('Inserisci il coefficiente b: '))
c = eval(input('Inserisci il coefficiente c: '))

# Calcola il delta
delta = b**2 - 4*a*c

# Crea una stringa formattata e leggibile che rappresenti l'equazione
equation = f'{a}x^2 + {b}x + {c} = 0'

if delta < 0:
    # In questo caso non ci sono soluzioni.
    print(f'L\'equazione {equation} non ha soluzioni reali.')
    # Usciamo prima di fare radici di numeri negativi!!!
else:
    # Allora ci sono soluzioni...
    if delta == 0:
        # Se il delta è 0 l'unica soluzione è semplice.
        x = -b/(2*a)
        print(f'L\'equazione {equation} ha una soluzione reale:')
        print(f'x = {x}.')
    else:
        # In questo caso ci sono due soluzioni che vanno calcolate.
        x1 = (-b+delta**.5)/(2*a)
        x2 = (-b-delta**.5)/(2*a)
        print(f'L\'equazione {equation} ha due soluzioni reali:')
        print(f'x1 = {x1}, x2 = {x2}.')

# Attendi un input dall'utente prima di chiudere...
input('Premi un tasto per uscire...')
