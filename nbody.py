import pygame
import math, random
import numpy as np

def random_position(width, height):
    return list(random.uniform(0, dimension) for dimension in (width, height))

def random_velocity(sigma):
    return list(random.normalvariate(0, sigma) for _ in range(2))

def random_state(width, height, sigma):
    return random_position(width, height), random_velocity(sigma)


class Particle:

    def __init__(self, s, v, m, density=1, color=(255, 255, 255)):
        
        self.s = np.array(s, dtype=float)
        self.v = np.array(v, dtype=float)
        self.a = np.array([0, 0], dtype=float)
        self.m = float(m)

        self.density = density
        self.radius = int(math.sqrt(self.m / (math.pi * self.density)))
        self.color = color

    def coordinates(self):
        return tuple(self.s.astype(int))

    def update(self, dt):
        self.s += self.v * dt
        self.v += self.a * dt
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.coordinates(), self.radius)


class System:

    def __init__(self, G, n, width, height, sigma, m, density=1, bg=(0, 0, 0)):

        self.G = G
        self.bg = bg
        
        self.particles = list()

        for i in range(n):

            s = random_position(width, height)
            v = random_velocity(sigma)
            
            particle = Particle(s, v, m, density=density)
            self.particles.append(particle)

    def translate(self, dx, dy):
        for p in self.particles:
            p.s += [dx, dy]

    def update(self, dt):

        for p in self.particles:
            p.a = np.array([0, 0], dtype=float)
        
        for i, p1 in enumerate(self.particles):
            for p2 in self.particles[i+1:]:
                ds = p2.s - p1.s
                d = np.linalg.norm(ds)
                f1 = self.G * p1.m * p2.m * ds / d**3
                f2 = -f1
                a1 = f1 / p1.m
                a2 = f2 / p2.m
                p1.a += a1
                p2.a += a2

        for p in self.particles:
            p.update(dt)

        groups = collide(self.particles)
        self.particles = []
        for g in groups:
            p = merge(g)
            self.particles.append(p)

    def draw(self, screen):

        screen.fill(self.bg)
        
        for p in self.particles:
            p.draw(screen)


def collide(particles):

    groups = []

    for i, p1 in enumerate(particles):

        group = None
        
        for g in groups:
            if p1 in g:
                group = g

        if not group:
            groups.append({p1, })
            group = groups[-1]
        
        for p2 in particles[i+1:]:
            if np.linalg.norm(p1.s - p2.s) < .8*max(p1.radius, p2.radius):
                group.add(p2)

    return groups


def merge(group):
    
    ss, vs, ms, ds = zip(*([p.s, p.v, p.m, p.density] for p in group))

    s = np.average(ss, axis=0, weights=ms)
    v = np.average(vs, axis=0, weights=ms)
    m = sum(ms)
    density = np.average(ds, axis=0, weights=ms)

    return Particle(s, v, m, density=density)


G = 1
n = int(input('Inserisci il numero di particelle: '))
size = width, height = (1365, 767)
sigma = 30
m = 1000000
density = 10000
bg = (0, 0, 0)

system = System(G, n, width, height, sigma, m, density=density, bg=bg)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

system.draw(screen)
pygame.display.flip()

drag_speed = 3

dt = 0.001
running = True
pause = False

while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            pause = not pause
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x <= 0:
        system.translate(drag_speed, 0)
    if mouse_x >= width:
        system.translate(-drag_speed, 0)
    if mouse_y <= 0:
        system.translate(0, drag_speed)
    if mouse_y >= height:
        system.translate(0, -drag_speed)
            
    if not pause:
        system.update(dt)
        system.draw(screen)
        pygame.display.flip() 
