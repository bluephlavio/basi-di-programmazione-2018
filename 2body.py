import sys, math, pygame
import numpy as np
from numpy.linalg import norm

class Particle:

    def __init__(self, s, v, m, color=(255, 255, 255), density=1):
        self.s = np.array(s, dtype=float)
        self.v = np.array(v, dtype=float)
        self.m = float(m)
        self.density = float(density)
        self.radius = int(math.sqrt(m / (math.pi * density)))
        self.color = color

    def update(self, force, dt=1):
        f = np.array(force, dtype=float)
        a = f / self.m
        self.v += a*dt
        self.s += self.v*dt

    def draw(self, observer=(0, 0)):
        pygame.draw.circle(screen, self.color, self.coordinates(), self.radius)

    def coordinates(self):
        return tuple(map(int, self.s))

    def __str__(self):
        return 's = {}\nv = {},\nm = {}'.format(self.s, self.v, self.m)



bg = (0, 0, 0)
size = width, height = (640, 480)
center = center_x, center_y = (width//2, height//2)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


scale = 1e9
G = 6.67e-11 * scale**-3
D = 1.5e11
d = D * scale**-1

m1 = 2e30
m2 = 6e29
m = m1 + m2

s1 = [center_x - m2*d/m, center_y]
s2 = [center_x + m1*d/m, center_y]

v2 = np.array([0, - 2.98e4 * scale**-1], dtype=float)
v1 = -m2/m1 * v2

d1 = 1.408e3 * scale**3
d2 = 5.515e3 * scale**3

p1 = Particle(s1, v1, m1, density=d1)
p2 = Particle(s2, v2, m2, density=d2)



running = True

while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    f1 = G*(p1.m*p2.m/norm(p2.s - p1.s)**3)*(p2.s - p1.s)
    f2 = -f1
    
    p1.update(f1, dt=86400)
    p2.update(f2, dt=86400)

    screen.fill(bg)
    p1.draw()
    p2.draw()
    pygame.display.flip()

