import sys, math, pygame
import numpy as np
from numpy.linalg import norm


class Particle:

    def __init__(self, s, v, m, density=1, color=(255, 255, 255)):
        self.s = np.array(s, dtype=float)
        self.v = np.array(v, dtype=float)
        self.m = float(m)
        self.density = density
        self.r = int(math.sqrt(m/(math.pi * density)))
        self.color = color

    def update(self, force, dt=1):
        a = np.array(force, dtype=float) / self.m
        self.v += a*dt
        self.s += self.v*dt

    def draw(self, screen, observer=(0, 0)):
        position = self.coordinates()
        color = self.redshift(observer)
        radius = self.r
        pygame.draw.circle(screen, color, position, radius)

    def coordinates(self):
        return tuple(map(int, self.s))
    
    def redshift(self, observer=(0, 0), redshift_factor=5e6):
        r, g, b = self.color
        point = np.array(observer, dtype=float)
        if not np.allclose(point, self.s):
            ds = self.s - point
            versor = ds / np.linalg.norm(ds)
            vrel = np.vdot(self.v, versor)
            redshift = min(int(redshift_factor * vrel), min(r, b))
            if redshift > 0:
                b -= redshift
            else:
                r += redshift
        return (r, g, b)

    def __str__(self):
        return 's = {}, v = {}, m = {}'.format(self.s, self.v, self.m)


class Observer:

    def __init__(self, position=(0, 0), color=(255, 255, 255), radius=10):
        self.position = position
        self.color = color
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def __str__(self):
        return 's = {}'.format(self.position)

bg = (0, 0, 0)
size = width, height = (640, 480)
center = center_x, center_y = (width//2, height//2)

scale = 6e8

G = 6.67e-11 * scale**-3
D = 1.5e11

d = D * scale**-1

m1 = 2e30
m2 = 6e29
m = m1 + m2

s1 = [center_x - m2*d/m, center_y]
s2 = [center_y + m1*d/m, center_y]

v2 = np.array([0., -math.sqrt(G*m/d)], dtype=float)
v1 = -m2/m1 * v2

d1 = 1.408e3 * scale**3
d2 = 5.515e3 * scale**3

p1 = Particle(s1, v1, m1, density=d1, color=(255, 100, 255))
p2 = Particle(s2, v2, m2, density=d2, color=(255, 100, 255))

p1.r = 20
p2.r = 5

o = Observer(position=(0, center_y), color=(255, 255, 255), radius=10)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

while running:

    clock.tick(50)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    f1 = G*(p1.m*p2.m/norm(p2.s - p1.s)**3)*(p2.s - p1.s)
    f2 = -f1
    
    p1.update(f1, dt=86400)
    p2.update(f2, dt=86400)

    screen.fill(bg)
    p1.draw(screen, observer=o.position)
    p2.draw(screen, observer=o.position)
    #o.draw(screen)
    pygame.display.flip()

