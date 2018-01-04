# Test per stabilire se un numero intero è primo

# Prende in input il numero da testare
n = int(input('Inserisci un numero: '))

# Inizializza la variabile booleana prime e la lista dei divisori
prime = True
dividers = []

# Cerca divisori fra 2 e n-1
for i in range(2, n):
    if n % i == 0:
        prime = False
        dividers.append(i)

# Stampa la primalità del numero
print('Il numero {} {} primo.'.format(n, 'è' if prime else 'non è'))

# Se il numero non è primo i suoi divisori vengono riportati
if not prime:
    print('I divisori sono: ', ', '.join(map(str, dividers)), '.', sep='')
