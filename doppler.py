import sys, pygame
import numpy as np
from numpy.linalg import norm


class Particle:

    def __init__(self, s, v, m, color=(255, 255, 255)):
        self.s = np.array(s, dtype=float)
        self.v = np.array(v, dtype=float)
        self.m = float(m)
        self.r = int(m)
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
    
    def redshift(self, observer=(0, 0), redshift_factor=100):
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


class Observer:

    def __init__(self, position, color, radius):
        self.position = position
        self.color = color
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)


bg = (0, 0, 0)
size = width, height = (640, 480)
center = center_x, center_y = (width//2, height//2)
G = 10
d = 100

p1 = Particle([size[0]/2-d/2, size[1]/2], [0, .4], 20, color=(255, 100, 255))
p2 = Particle([size[0]/2+d/2, size[1]/2], [0, -.8], 10, color=(255, 100, 255))

o = Observer((300, 10), (255, 255, 255), 10)

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
    
    p1.update(f1)
    p2.update(f2)

    screen.fill(bg)
    p1.draw(screen, observer=o.position)
    p2.draw(screen, observer=o.position)
    o.draw(screen)
    pygame.display.flip()

