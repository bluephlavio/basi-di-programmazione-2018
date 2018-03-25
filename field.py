import pygame
import math
import random

# FISICA
G = 1
M = 100
mu = G * M
numero_particelle = 100
sigma_p = 100
sigma_v = 1

# DIMENSIONI
dimensioni = (640, 480)
centro = (dimensioni[0]//2, dimensioni[1]//2)
raggio_particella = 10
diametro_particella = 2 * raggio_particella
dimensioni_particella = (diametro_particella, ) * 2

# IMMAGINI
icona = pygame.image.load('img\\icon.jpg')
icona = pygame.transform.smoothscale(icona, (32, 32))
sfondo = pygame.image.load('img\\bg-light.jpg')
sfondo = pygame.transform.smoothscale(sfondo, (dimensioni))
particella = pygame.image.load('img\\star.png')
particella = pygame.transform.smoothscale(particella, dimensioni_particella)

# SCHERMO
pygame.display.set_mode(dimensioni)
pygame.display.set_caption('Field')
pygame.display.set_icon(icona)
schermo = pygame.display.get_surface()

# CLASSI

class Particella:

    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def aggiorna(self, dt=1, attrattore=(0, 0)):
        x = self.pos[0]
        y = self.pos[1]
        dx = x - attrattore[0]
        dy = y - attrattore[1]
        r = math.sqrt(dx**2 + dy**2)
        a = - mu / r**2
        ax = a * dx / r
        ay = a * dy / r
        self.pos[0] += self.vel[0] * dt
        self.pos[1] += self.vel[1] * dt
        self.vel[0] += ax * dt
        self.vel[1] += ay * dt

    def disegna(self, schermo):
        x = int(self.pos[0]) - raggio_particella
        y = int(self.pos[1]) - raggio_particella
        schermo.blit(particella, (x, y))


class Sistema:

    def __init__(self, n=100, centro=(0, 0), sigma_p=100, sigma_v=1):
        self.particelle = []
        for i in range(n):
            x = random.gauss(centro[0], sigma_p)
            y = random.gauss(centro[1], sigma_p)
            vx = random.gauss(0, sigma_v)
            vy = random.gauss(0,sigma_v)
            particella = Particella([x, y], [vx, vy])
            self.particelle.append(particella)

    def aggiorna(self, dt=1, attrattore=(0, 0)):
        for p in self.particelle:
            p.aggiorna(dt, attrattore=attrattore)

    def disegna(self, schermo):
        for p in self.particelle:
            p.disegna(schermo)

# OGGETTI

sistema = Sistema(
    n=numero_particelle,
    centro=centro,
    sigma_p=sigma_p,
    sigma_v=sigma_v
    )

# MAIN LOOP
running = True
while running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    sistema.aggiorna(dt=1, attrattore=centro)

    schermo.blit(sfondo, (0, 0))
    sistema.disegna(schermo)

    pygame.display.flip()
