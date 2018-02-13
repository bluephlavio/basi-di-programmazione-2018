# Test per stabilire se un numero intero è primo

import math
import time

# Prende in input il numero da testare
n = int(input('Inserisci un numero intero: '))

t1 = time.time()

# Inizializza la variabile booleana 'primo' e la lista 'divisori'
primo = True
divisori = []

# Cerca divisori fra 2 e n-1
for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
        primo = False
        divisori.append(i)
        divisori.append(n//i)

# Stampa la primalità del numero
print(f'Il numero {n} {"è" if primo else "non è"} primo.')

# Se il numero non è primo, la lista dei suoi divisori viene stampata
if not primo:
    divisori.sort() # riordina la lista dei divisori in ordine crescente
    print(f'Ho trovato {len(divisori)} divisori {str(divisori)}.')

t2 = time.time()
dt = t2 - t1
print(f'\nCi ho messo {dt} secondi!')
input('\nPremi un tasto per uscire...')
