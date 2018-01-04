import math
from random import gauss

mu = eval(input('mu: '))
sigma = eval(input('sigma: '))
n = eval(input('n: '))

print('-'*50)

data = [gauss(mu, sigma) for i in range(n)]

print('Dati')
print(', '.join(map(str, data)))

mean = 0
for x in data:
    mean += x / n

var = 0
for x in data:
    var += (x - mean)**2 / n

dev = math.sqrt(var)

xmin = min(data)
xmax = max(data)

disp = (xmax- xmin) / 2

print('-'*50)
print('Risultati')
print('Media:', mean)
print('Varianza:', var)
print('Devizione standard:', dev)
print('Minimo:', xmin)
print('Massimo:', xmax)
print('Semidispersione:', disp)

