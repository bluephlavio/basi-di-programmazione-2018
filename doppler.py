import sys, pygame
import numpy as np
from numpy.linalg import norm

bg = (0, 0, 0)
size = width, height = (640, 480)
center = center_x, center_y = (width//2, height//2)
G = 10
d = 100

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

class Particle:

    def __init__(self, s, v, m, color=(255, 255, 255)):
        self.s = np.array(s, dtype=float)
        self.v = np.array(v, dtype=float)
        self.m = float(m)
        self.r = int(m)
        self.color = color

    def move(self, force, dt=1):
        a = np.array(force, dtype=float) / self.m
        self.v += a*dt
        self.s += self.v*dt

    def draw(self, observer=(0, 0)):
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


p1 = Particle([size[0]/2-d/2, size[1]/2], [0, .4], 20, color=(255, 100, 255))
p2 = Particle([size[0]/2+d/2, size[1]/2], [0, -.8], 10, color=(255, 100, 255))
    

running = True

while running:

    clock.tick(50)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    f1 = G*(p1.m*p2.m/norm(p2.s - p1.s)**3)*(p2.s - p1.s)
    f2 = -f1
    
    p1.move(f1)
    p2.move(f2)

    screen.fill(bg)
    p1.draw()
    p2.draw()
    pygame.display.flip()

