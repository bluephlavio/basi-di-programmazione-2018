import numpy as np
from universe import *

# DIMENSIONI
width = 500
height = 500
size = (width, height)

# SCHERMO
pygame.display.set_mode(size)
pygame.display.set_caption('Corrente')
screen = pygame.display.get_surface()

# FISICA
n = 100
sigma = 0.5
drift = [0, 0]

def drift_gen(sigma, drift):
    normal_gen = normal_2d_gen(mu=0, sigma=sigma)
    while True:
        yield next(normal_gen) + np.array(drift)

class Electrons(System):

    def __init__(self, n, world):
        self.width = world[0]
        self.height = world[1]
        pos_gen = uniform_2d_gen([0, 0], world)
        vel_gen = drift_gen(sigma, drift)
        super().__init__(n, pos_gen, vel_gen)

    def update(self, dt=1):
        super().update(dt=dt)
        for p in self.particles:
            if p.s[0] > self.width:
                p.s[0] = 0
            if p.s[0] < 0:
                p.s[0] = self.width
            if p.s[1] > self.height:
                p.s[1] = 0
            if p.s[1] < 0:
                p.s[1] = self.height


system = Electrons(100, size)

# MAIN LOOP
running = True
while running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    system.update()
    system.draw(screen)
    pygame.display.flip()
