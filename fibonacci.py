# Genera i primi n numeri di Fibonacci

# Richiedi quanti numeri l'utente vuole...
n = int(input('Quanti numeri di Fibonacci vuoi? '))

# Inizializza una lista dei numeri di Fibonacci
fib = [1, 1]

# Calcola i successivi numeri di Fibonacci
for i in range(2, n):
	fib += [fib[i-1] + fib[i-2]]

# Stampa i numeri calcolati
print('i\tfib(i)') # Intestazione
for i in range(n):
	print(f'{i+1}\t{fib[i]}')

print('Sto preparando il grafico, attendi...')

# Grafico della successione

# Importiamo il modulo matplotlib necessario alla creazione di grafici.
import matplotlib.pyplot as plt

# Impostiamo titolo, assi, etc..
plt.figure('Fibonacci')
plt.title('$f_n=f_{n-2}+f_{n-1}$, $f_1=%d$, $f_2=%d$' % (1, 1))
plt.xlabel('$n$')
plt.ylabel('$f_n$')
plt.grid(True)

# Creazione (plot) del grafico
plt.plot(range(1, n+1), fib, 'bo')

# Mostra a schermo il grafico
plt.show()

