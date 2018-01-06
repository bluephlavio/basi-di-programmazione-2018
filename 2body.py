import sys, pygame
import numpy as np
from numpy.linalg import norm

G = 10
d = 100

pygame.init()

bg = (0, 0, 0)
size = (640, 480)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

class Particle:

    def __init__(self, s, v, m, color=(100,100,100)):
        self.s = np.array(s, dtype=float)
        self.v = np.array(v, dtype=float)
        self.m = float(m)
        self.r = int(m)
        self.color = color

    def move(self, force, dt=1):
        a = np.array(force, dtype=float) / self.m
        self.v += a*dt
        self.s += self.v*dt

    def draw(self):
        x, y = map(int, self.s)
        pygame.draw.circle(screen, self.color, (x, y), self.r)


p1 = Particle([size[0]/2-d/2, size[1]/2], [0, .4], 20)
p2 = Particle([size[0]/2+d/2, size[1]/2], [0, -.8], 10)
    

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

