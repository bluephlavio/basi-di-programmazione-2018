# Genera i primi n numeri di Fibonacci

import sys

f1 = int(sys.argv[1])
f2 = int(sys.argv[2])
N = int(sys.argv[3])

def fib1(a, b, n):
    print(1, a)
    print(2, b)
    for i in range(2, n):
        c = a + b
        print(i + 1, c)
        a = b
        b = c


def fib2(a, b, n):
    fib = [a, b]
    for i in range(2, n):
        fib.append(fib[i-2] + fib[i-1])
    return fib


fib = fib2(f1, f2, N)
for i, f in enumerate(fib):
    print(i + 1, f)

import matplotlib.pyplot as plt

plt.figure('Fibonacci')
plt.title('$f_n=f_{n-2}+f_{n-1}$, $f_1=%d$, $f_2=%d$' % (f1, f2))
plt.xlabel('$n$')
plt.ylabel('$f_n$')
plt.grid(True)

plt.plot(range(1, N+1), fib, 'bo')

plt.show()

