# Calcola il quadrato di un numero intero

while True:
    try:
        n = int(input('Inserisci un numero intero: '))
        break
    except ValueError:
        print('ERRORE: non sono riuscito ad interpretare il valore inserito come un numero intero.')
        continue

print(f'Il quadrato di {n} è {n**2}.')
input('Premi un tasto per uscire...')
