import pygame
import random
import csv
import matplotlib.pyplot as plt
import numpy as np
import time

# DIMENSIONI
dimensioni = (640, 480)
raggio_particella = 10
diametro_particella = 2 * raggio_particella
dimensioni_particella = (diametro_particella,) * 2

# FISICA
n = 10
sigma_v = 2
g = 0

# ANALISI DATI
analisi = True
frequenza = 10
bins = 25
x_range=(0, dimensioni[0])
y_range=(0, dimensioni[1])
vx_range=(-10 * sigma_v, 10 * sigma_v)
vy_range=(-10 * sigma_v, 10 * sigma_v)
v2_range=(0, 3 * sigma_v**2)

if analisi:
    fig = plt.figure('stats')
    ax_1 = plt.subplot(321)
    ax_2 = plt.subplot(322)
    ax_3 = plt.subplot(323)
    ax_4 = plt.subplot(324)
    ax_5 = plt.subplot(313)
    plt.ion()
    plt.show()


# FUNZIONI
def carica_immagine(nome_file, dimensioni):
    img = pygame.image.load(f'img\{nome_file}')
    img = pygame.transform.smoothscale(img, dimensioni)
    return img

def plot(universo):
    x = [p.s[0] for p in universo.particelle]
    y = [p.s[1] for p in universo.particelle]
    vx = [p.v[0] for p in universo.particelle]
    vy = [p.v[1] for p in universo.particelle]
    v2 = [p.v[0]**2+p.v[1]**2 for p in universo.particelle]

    ax_1.clear()
    ax_1.hist(x, bins=bins, range=x_range)
    ax_1.set_xlabel('$x$')
    ax_1.set_ylabel('$n$')
    
    ax_2.clear()
    ax_2.hist(y, bins=bins, range=y_range)
    ax_2.set_xlabel('$y$')
    ax_2.set_ylabel('$n$')
    
    ax_3.clear()
    ax_3.hist(vx, bins=bins, range=vx_range)
    ax_3.set_xlabel('$v_x$')
    ax_3.set_ylabel('$n$')
    
    ax_4.clear()
    ax_4.hist(vy, bins=bins, range=vy_range)
    ax_4.set_xlabel('$v_y$')
    ax_4.set_ylabel('$n$')
    
    ax_5.clear()
    ax_5.hist(v2, bins=bins, range=v2_range)
    ax_5.set_xlabel('$v^2$')
    ax_5.set_ylabel('$n$')
    
    plt.tight_layout()
    fig.canvas.flush_events()

# IMMAGINI
icona = carica_immagine('icon.jpg', (32, 32))
sfondo = carica_immagine('bg-light.jpg', dimensioni)
particella = carica_immagine('star.png', dimensioni_particella)

# CLASSI

class Particella:

    def __init__(self, s, v):
        self.s = s
        self.v = v

    def pos(self):
        return (self.s[0], self.s[1])

    def vel(self):
        return (self.v[0], self.v[1])

    def muovi(self, dt=1, scatola=None):
        vx, vy = self.vel()
        self.s[0] += vx * dt
        self.s[1] += vy * dt
        urto = False
        if scatola:
            x, y = self.pos()
            larghezza = scatola[0]
            altezza = scatola[1]
            if (x < 0 and vx < 0) or (x > larghezza and vx > 0):
                self.v[0] = -self.v[0]
                urto = True
            if (y < 0 and vy < 0) or (y > altezza and vy > 0):
                self.v[1] = -self.v[1]
                urto = True
        if not urto:
            self.v[1] += g * dt

    def disegna(self, schermo):
        x = int(self.s[0]) - raggio_particella
        y = int(self.s[1]) - raggio_particella
        schermo.blit(particella, (x, y))


class Universo:

    def __init__(self, n, sigma_v, dimensioni=dimensioni):
        self.dimensioni = dimensioni
        self.particelle = []
        for i in range(n):
            x = random.uniform(0, dimensioni[0])
            y = random.uniform(0, dimensioni[1])
            vx = random.gauss(0, sigma_v)
            vy = random.gauss(0, sigma_v)
            pos = [x, y]
            vel = [vx, vy]
            p = Particella(pos, vel)
            self.particelle.append(p)

    def evolvi(self, dt=1):
        for p in self.particelle:
            p.muovi(dt=dt, scatola=self.dimensioni)

    def disegna(self, schermo):
        for p in self.particelle:
            p.disegna(schermo)


# SCHERMO
pygame.display.set_mode(dimensioni, pygame.RESIZABLE)
pygame.display.set_caption('Gas')
pygame.display.set_icon(icona)
schermo = pygame.display.get_surface()

# TEMPO
tempo = pygame.time.Clock()
t = time.time()
t0 = t

# OGGETTI
universo = Universo(n, sigma_v, dimensioni=dimensioni)

running = True
while running:

    tempo.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.VIDEORESIZE:
            dimensioni = e.size
            pygame.display.set_mode(dimensioni, pygame.RESIZABLE)
            schermo = pygame.display.get_surface()

    t = time.time()
    dt = t - t0
    if analisi and dt > (1 / frequenza):
        plot(universo)
        t0 = t

    universo.evolvi()

    schermo.blit(sfondo, (0,0))
    universo.disegna(schermo)

    pygame.display.flip()
