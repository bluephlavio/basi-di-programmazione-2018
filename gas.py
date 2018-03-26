import pygame
import random

# FISICA
n = 100
sigma_v = 25
g = 10
dt = 0.1

# DIMENSIONI
dimensioni = (640, 480)
raggio_particella = 10
diametro_particella = 2 * raggio_particella
dimensioni_particella = (diametro_particella,) * 2

# FUNZIONI
def carica_immagine(nome_file, dimensioni):
    img = pygame.image.load(f'img\{nome_file}')
    img = pygame.transform.smoothscale(img, dimensioni)
    return img

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
        x = self.s[0] - raggio_particella
        y = self.s[1] - raggio_particella
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

    universo.evolvi(dt=dt)

    schermo.blit(sfondo, (0,0))
    universo.disegna(schermo)

    pygame.display.flip()
